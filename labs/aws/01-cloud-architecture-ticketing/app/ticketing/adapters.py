"""DynamoDB and SQS adapters for the local AWS-shaped environment."""

from __future__ import annotations

import json
import time
import uuid
from typing import Any

import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from botocore.exceptions import ClientError

from .config import Settings
from .domain import IdempotencyConflict, ReservationRequest, SeatUnavailable

_serializer = TypeSerializer()
_deserializer = TypeDeserializer()


def _encode_item(item: dict[str, Any]) -> dict[str, dict]:
    return {key: _serializer.serialize(value) for key, value in item.items()}


def _decode_item(item: dict[str, dict] | None) -> dict[str, Any] | None:
    if item is None:
        return None
    return {key: _deserializer.deserialize(value) for key, value in item.items()}


class DynamoTicketStore:
    """Persistence adapter whose transactions enforce reservation ownership."""

    def __init__(self, config: Settings) -> None:
        self.config = config
        self.client = boto3.client(
            "dynamodb",
            region_name=config.region,
            endpoint_url=config.dynamodb_endpoint,
        )

    @staticmethod
    def seat_key(event_id: str, seat_id: str) -> str:
        return f"{event_id}#{seat_id}"

    def ready(self) -> bool:
        expected = {
            self.config.inventory_table,
            self.config.orders_table,
            self.config.idempotency_table,
        }
        existing = set(self.client.list_tables().get("TableNames", []))
        return expected.issubset(existing)

    def get_event(self, event_id: str) -> dict[str, Any]:
        response = self.client.scan(
            TableName=self.config.inventory_table,
            FilterExpression="event_id = :event_id",
            ExpressionAttributeValues={":event_id": {"S": event_id}},
            ProjectionExpression="seat_id, #state",
            ExpressionAttributeNames={"#state": "state"},
        )
        seats = [_decode_item(item) for item in response.get("Items", [])]
        if not seats:
            raise KeyError(event_id)
        available = sum(1 for seat in seats if seat and seat["state"] == "AVAILABLE")
        return {
            "eventId": event_id,
            "seatCount": len(seats),
            "availableCount": available,
        }

    def reserve(
        self, request: ReservationRequest, idempotency_key: str
    ) -> tuple[dict[str, Any], bool]:
        previous = self._get_idempotency(idempotency_key)
        if previous:
            return self._replay(previous, request)

        now = int(time.time())
        order_id = str(uuid.uuid4())
        expires_at = now + self.config.hold_seconds
        order = {
            "order_id": order_id,
            "event_id": request.event_id,
            "seat_id": request.seat_id,
            "status": "RESERVED",
            "payment_mode": request.payment_mode,
            "dispatch_status": "PENDING",
            "hold_expires_at": expires_at,
            "created_at": now,
        }
        idempotency = {
            "idempotency_key": idempotency_key,
            "fingerprint": request.fingerprint,
            "order_id": order_id,
            "created_at": now,
        }

        try:
            self.client.transact_write_items(
                TransactItems=[
                    {
                        "Put": {
                            "TableName": self.config.idempotency_table,
                            "Item": _encode_item(idempotency),
                            "ConditionExpression": (
                                "attribute_not_exists(idempotency_key)"
                            ),
                        }
                    },
                    {
                        "Update": {
                            "TableName": self.config.inventory_table,
                            "Key": _encode_item(
                                {
                                    "seat_key": self.seat_key(
                                        request.event_id, request.seat_id
                                    )
                                }
                            ),
                            "UpdateExpression": (
                                "SET #state = :held, order_id = :order_id, "
                                "hold_expires_at = :expires_at"
                            ),
                            "ConditionExpression": (
                                "attribute_exists(seat_key) AND "
                                "(#state = :available OR "
                                "(#state = :held AND hold_expires_at <= :now))"
                            ),
                            "ExpressionAttributeNames": {"#state": "state"},
                            "ExpressionAttributeValues": _encode_item(
                                {
                                    ":held": "HELD",
                                    ":available": "AVAILABLE",
                                    ":order_id": order_id,
                                    ":expires_at": expires_at,
                                    ":now": now,
                                }
                            ),
                        }
                    },
                    {
                        "Put": {
                            "TableName": self.config.orders_table,
                            "Item": _encode_item(order),
                            "ConditionExpression": "attribute_not_exists(order_id)",
                        }
                    },
                ]
            )
            return order, False
        except ClientError as error:
            if error.response["Error"]["Code"] != "TransactionCanceledException":
                raise
            previous = self._get_idempotency(idempotency_key)
            if previous:
                return self._replay(previous, request)
            raise SeatUnavailable("seat is already held or confirmed") from error

    def get_order(self, order_id: str) -> dict[str, Any] | None:
        response = self.client.get_item(
            TableName=self.config.orders_table,
            Key=_encode_item({"order_id": order_id}),
            ConsistentRead=True,
        )
        return _decode_item(response.get("Item"))

    def mark_dispatched(self, order_id: str) -> None:
        self.client.update_item(
            TableName=self.config.orders_table,
            Key=_encode_item({"order_id": order_id}),
            UpdateExpression="SET dispatch_status = :sent",
            ExpressionAttributeValues=_encode_item({":sent": "SENT"}),
        )

    def mark_reconciliation(self, order_id: str) -> None:
        self.client.update_item(
            TableName=self.config.orders_table,
            Key=_encode_item({"order_id": order_id}),
            UpdateExpression="SET #status = :reconciliation",
            ConditionExpression="#status <> :confirmed AND #status <> :declined",
            ExpressionAttributeNames={"#status": "status"},
            ExpressionAttributeValues=_encode_item(
                {
                    ":reconciliation": "RECONCILIATION",
                    ":confirmed": "CONFIRMED",
                    ":declined": "DECLINED",
                }
            ),
        )

    def list_pending_dispatches(self, limit: int = 25) -> list[dict[str, Any]]:
        return self._scan_orders(
            "dispatch_status = :pending AND #status = :reserved",
            {"#status": "status"},
            {":pending": "PENDING", ":reserved": "RESERVED"},
            limit,
        )

    def list_reconciliation(self, limit: int = 25) -> list[dict[str, Any]]:
        return self._scan_orders(
            "#status = :reconciliation",
            {"#status": "status"},
            {":reconciliation": "RECONCILIATION"},
            limit,
        )

    def confirm(self, order: dict[str, Any]) -> None:
        self.client.transact_write_items(
            TransactItems=[
                {
                    "Update": {
                        "TableName": self.config.orders_table,
                        "Key": _encode_item({"order_id": order["order_id"]}),
                        "UpdateExpression": "SET #status = :confirmed",
                        "ConditionExpression": "#status <> :declined",
                        "ExpressionAttributeNames": {"#status": "status"},
                        "ExpressionAttributeValues": _encode_item(
                            {":confirmed": "CONFIRMED", ":declined": "DECLINED"}
                        ),
                    }
                },
                {
                    "Update": {
                        "TableName": self.config.inventory_table,
                        "Key": _encode_item(
                            {
                                "seat_key": self.seat_key(
                                    order["event_id"], order["seat_id"]
                                )
                            }
                        ),
                        "UpdateExpression": "SET #state = :confirmed",
                        "ConditionExpression": "order_id = :order_id",
                        "ExpressionAttributeNames": {"#state": "state"},
                        "ExpressionAttributeValues": _encode_item(
                            {
                                ":confirmed": "CONFIRMED",
                                ":order_id": order["order_id"],
                            }
                        ),
                    }
                },
            ]
        )

    def decline(self, order: dict[str, Any]) -> None:
        self.client.transact_write_items(
            TransactItems=[
                {
                    "Update": {
                        "TableName": self.config.orders_table,
                        "Key": _encode_item({"order_id": order["order_id"]}),
                        "UpdateExpression": "SET #status = :declined",
                        "ConditionExpression": "#status <> :confirmed",
                        "ExpressionAttributeNames": {"#status": "status"},
                        "ExpressionAttributeValues": _encode_item(
                            {":declined": "DECLINED", ":confirmed": "CONFIRMED"}
                        ),
                    }
                },
                {
                    "Update": {
                        "TableName": self.config.inventory_table,
                        "Key": _encode_item(
                            {
                                "seat_key": self.seat_key(
                                    order["event_id"], order["seat_id"]
                                )
                            }
                        ),
                        "UpdateExpression": (
                            "SET #state = :available REMOVE order_id, hold_expires_at"
                        ),
                        "ConditionExpression": (
                            "attribute_not_exists(order_id) OR order_id = :order_id"
                        ),
                        "ExpressionAttributeNames": {"#state": "state"},
                        "ExpressionAttributeValues": _encode_item(
                            {
                                ":available": "AVAILABLE",
                                ":order_id": order["order_id"],
                            }
                        ),
                    }
                },
            ]
        )

    def _get_idempotency(self, idempotency_key: str) -> dict[str, Any] | None:
        response = self.client.get_item(
            TableName=self.config.idempotency_table,
            Key=_encode_item({"idempotency_key": idempotency_key}),
            ConsistentRead=True,
        )
        return _decode_item(response.get("Item"))

    def _replay(
        self, idempotency: dict[str, Any], request: ReservationRequest
    ) -> tuple[dict[str, Any], bool]:
        if idempotency["fingerprint"] != request.fingerprint:
            raise IdempotencyConflict("idempotency key belongs to a different request")
        order = self.get_order(idempotency["order_id"])
        if order is None:
            raise RuntimeError("idempotency record refers to a missing order")
        return order, True

    def _scan_orders(
        self,
        expression: str,
        names: dict[str, str],
        values: dict[str, Any],
        limit: int,
    ) -> list[dict[str, Any]]:
        response = self.client.scan(
            TableName=self.config.orders_table,
            FilterExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=_encode_item(values),
            Limit=limit,
        )
        return [_decode_item(item) for item in response.get("Items", [])]


class SqsOrderQueue:
    """Small SQS adapter; duplicate delivery remains an expected condition."""

    def __init__(self, config: Settings) -> None:
        self.config = config
        self.client = boto3.client(
            "sqs", region_name=config.region, endpoint_url=config.sqs_endpoint
        )
        self._queue_url: str | None = None

    @property
    def queue_url(self) -> str:
        if self._queue_url is None:
            response = self.client.get_queue_url(QueueName=self.config.queue_name)
            self._queue_url = response["QueueUrl"]
        return self._queue_url

    def ready(self) -> bool:
        try:
            self.client.get_queue_attributes(
                QueueUrl=self.queue_url, AttributeNames=["QueueArn"]
            )
            return True
        except ClientError:
            return False

    def publish(self, order_id: str) -> str:
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps({"order_id": order_id}),
        )
        return response["MessageId"]

    def receive(self, wait_seconds: int) -> list[dict[str, Any]]:
        response = self.client.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=5,
            WaitTimeSeconds=wait_seconds,
            VisibilityTimeout=15,
            AttributeNames=["ApproximateReceiveCount"],
        )
        return response.get("Messages", [])

    def delete(self, receipt_handle: str) -> None:
        self.client.delete_message(
            QueueUrl=self.queue_url, ReceiptHandle=receipt_handle
        )
