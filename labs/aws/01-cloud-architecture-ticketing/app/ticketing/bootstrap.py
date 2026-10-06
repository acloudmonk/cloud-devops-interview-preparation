"""Create local DynamoDB tables, queues, redrive policy, and sample seats."""

from __future__ import annotations

import json
import logging
import time

import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

from .adapters import _encode_item
from .config import settings

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("ticketing.bootstrap")


def _wait_for_dependencies() -> tuple:
    dynamodb = boto3.client(
        "dynamodb",
        region_name=settings.region,
        endpoint_url=settings.dynamodb_endpoint,
    )
    sqs = boto3.client(
        "sqs", region_name=settings.region, endpoint_url=settings.sqs_endpoint
    )
    for attempt in range(30):
        try:
            dynamodb.list_tables()
            sqs.list_queues()
            return dynamodb, sqs
        except (ClientError, EndpointConnectionError):
            if attempt == 29:
                raise
            time.sleep(2)
    raise RuntimeError("local dependencies did not become ready")


def _create_table(dynamodb, table_name: str, key_name: str) -> None:
    existing = dynamodb.list_tables().get("TableNames", [])
    if table_name in existing:
        return
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": key_name, "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": key_name, "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )
    dynamodb.get_waiter("table_exists").wait(TableName=table_name)
    logger.info("created table %s", table_name)


def _create_queues(sqs) -> None:
    dlq_url = sqs.create_queue(QueueName=settings.dlq_name)["QueueUrl"]
    dlq_arn = sqs.get_queue_attributes(QueueUrl=dlq_url, AttributeNames=["QueueArn"])[
        "Attributes"
    ]["QueueArn"]
    redrive_policy = json.dumps(
        {"deadLetterTargetArn": dlq_arn, "maxReceiveCount": "3"}
    )
    sqs.create_queue(
        QueueName=settings.queue_name,
        Attributes={
            "RedrivePolicy": redrive_policy,
            "VisibilityTimeout": "15",
            "ReceiveMessageWaitTimeSeconds": "5",
        },
    )
    logger.info("created or verified queues")


def _seed_inventory(dynamodb) -> None:
    for seat_number in range(1, 21):
        seat_id = f"seat-{seat_number:03d}"
        try:
            dynamodb.put_item(
                TableName=settings.inventory_table,
                Item=_encode_item(
                    {
                        "seat_key": f"event-001#{seat_id}",
                        "event_id": "event-001",
                        "seat_id": seat_id,
                        "state": "AVAILABLE",
                    }
                ),
                ConditionExpression="attribute_not_exists(seat_key)",
            )
        except ClientError as error:
            if error.response["Error"]["Code"] != "ConditionalCheckFailedException":
                raise


def main() -> None:
    dynamodb, sqs = _wait_for_dependencies()
    _create_table(dynamodb, settings.inventory_table, "seat_key")
    _create_table(dynamodb, settings.orders_table, "order_id")
    _create_table(dynamodb, settings.idempotency_table, "idempotency_key")
    _create_queues(sqs)
    _seed_inventory(dynamodb)
    logger.info("local ticketing dependencies are initialized")


if __name__ == "__main__":
    main()
