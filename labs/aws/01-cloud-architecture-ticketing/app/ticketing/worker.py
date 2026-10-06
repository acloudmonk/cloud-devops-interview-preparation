"""Order dispatcher, payment worker, and reconciliation loop."""

from __future__ import annotations

import json
import logging
import time

import httpx

from .adapters import DynamoTicketStore, SqsOrderQueue
from .config import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger("ticketing.worker")
store = DynamoTicketStore(settings)
queue = SqsOrderQueue(settings)


def dispatch_pending() -> None:
    for order in store.list_pending_dispatches():
        try:
            queue.publish(order["order_id"])
            store.mark_dispatched(order["order_id"])
            logger.info("dispatched pending order order_id=%s", order["order_id"])
        except Exception:
            logger.exception("pending dispatch failed order_id=%s", order["order_id"])


def reconcile_payments(client: httpx.Client) -> None:
    for order in store.list_reconciliation():
        try:
            response = client.get(
                f"{settings.payment_url}/payments/{order['order_id']}"
            )
            if response.status_code == 404:
                continue
            response.raise_for_status()
            outcome = response.json()["status"]
            if outcome == "charged":
                store.confirm(order)
            elif outcome == "declined":
                store.decline(order)
            logger.info(
                "reconciled payment order_id=%s outcome=%s",
                order["order_id"],
                outcome,
            )
        except Exception:
            logger.exception(
                "payment reconciliation failed order_id=%s", order["order_id"]
            )


def process_message(message: dict, client: httpx.Client) -> None:
    try:
        order_id = json.loads(message["Body"])["order_id"]
    except (KeyError, TypeError, ValueError):
        logger.error("invalid order message left for redrive")
        return

    order = store.get_order(order_id)
    if order is None:
        logger.error("unknown order left for redrive order_id=%s", order_id)
        return
    if order["status"] in {"CONFIRMED", "DECLINED"}:
        queue.delete(message["ReceiptHandle"])
        return

    try:
        response = client.post(
            f"{settings.payment_url}/payments",
            headers={"Idempotency-Key": order_id},
            json={"order_id": order_id, "mode": order["payment_mode"]},
        )
        if response.status_code >= 500:
            store.mark_reconciliation(order_id)
        else:
            response.raise_for_status()
            outcome = response.json()["status"]
            if outcome == "charged":
                store.confirm(order)
            elif outcome == "declined":
                store.decline(order)
            else:
                store.mark_reconciliation(order_id)
        queue.delete(message["ReceiptHandle"])
    except (httpx.TimeoutException, httpx.NetworkError):
        store.mark_reconciliation(order_id)
        queue.delete(message["ReceiptHandle"])
        logger.warning("payment outcome unknown order_id=%s", order_id)
    except Exception:
        logger.exception("order processing failed order_id=%s", order_id)
        latest = store.get_order(order_id)
        if latest and latest["status"] in {"CONFIRMED", "DECLINED"}:
            queue.delete(message["ReceiptHandle"])


def main() -> None:
    logger.info("worker started")
    with httpx.Client(timeout=settings.payment_timeout_seconds) as client:
        while True:
            dispatch_pending()
            reconcile_payments(client)
            for message in queue.receive(settings.worker_wait_seconds):
                process_message(message, client)
            time.sleep(1)


if __name__ == "__main__":
    main()
