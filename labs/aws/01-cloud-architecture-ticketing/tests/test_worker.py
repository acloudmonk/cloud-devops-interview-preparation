from __future__ import annotations

import json
import os
import pathlib
import sys
import unittest

os.environ.setdefault("AWS_ACCESS_KEY_ID", "local")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "local")
os.environ.setdefault("AWS_EC2_METADATA_DISABLED", "true")

APP_ROOT = pathlib.Path(__file__).resolve().parents[1] / "app"
sys.path.insert(0, str(APP_ROOT))

from ticketing import worker  # noqa: E402


class FakeResponse:
    def __init__(self, status_code: int, payload: dict | None = None) -> None:
        self.status_code = status_code
        self._payload = payload or {}

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self) -> dict:
        return self._payload


class FakePaymentClient:
    def __init__(self, response: FakeResponse) -> None:
        self.response = response
        self.calls = 0

    def post(self, *args, **kwargs) -> FakeResponse:
        self.calls += 1
        return self.response


class FakeQueue:
    def __init__(self) -> None:
        self.deleted: list[str] = []

    def delete(self, receipt_handle: str) -> None:
        self.deleted.append(receipt_handle)


class FakeWorkerStore:
    def __init__(self, status: str = "RESERVED") -> None:
        self.order = {
            "order_id": "order-001",
            "event_id": "event-001",
            "seat_id": "seat-001",
            "status": status,
            "payment_mode": "success",
        }
        self.confirmed = 0
        self.reconciliation = 0

    def get_order(self, order_id: str):
        return self.order if order_id == self.order["order_id"] else None

    def confirm(self, order: dict) -> None:
        self.confirmed += 1
        self.order["status"] = "CONFIRMED"

    def decline(self, order: dict) -> None:
        self.order["status"] = "DECLINED"

    def mark_reconciliation(self, order_id: str) -> None:
        self.reconciliation += 1
        self.order["status"] = "RECONCILIATION"


class WorkerContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = FakeQueue()
        worker.queue = self.queue
        self.message = {
            "Body": json.dumps({"order_id": "order-001"}),
            "ReceiptHandle": "receipt-001",
        }

    def test_successful_charge_confirms_and_acknowledges(self) -> None:
        store = FakeWorkerStore()
        worker.store = store
        client = FakePaymentClient(FakeResponse(200, {"status": "charged"}))

        worker.process_message(self.message, client)

        self.assertEqual(1, store.confirmed)
        self.assertEqual(["receipt-001"], self.queue.deleted)

    def test_ambiguous_provider_response_enters_reconciliation(self) -> None:
        store = FakeWorkerStore()
        worker.store = store
        client = FakePaymentClient(FakeResponse(504))

        worker.process_message(self.message, client)

        self.assertEqual(1, store.reconciliation)
        self.assertEqual(["receipt-001"], self.queue.deleted)

    def test_duplicate_terminal_delivery_does_not_charge_again(self) -> None:
        store = FakeWorkerStore(status="CONFIRMED")
        worker.store = store
        client = FakePaymentClient(FakeResponse(200, {"status": "charged"}))

        worker.process_message(self.message, client)

        self.assertEqual(0, client.calls)
        self.assertEqual(["receipt-001"], self.queue.deleted)

    def test_invalid_message_is_left_for_dlq_redrive(self) -> None:
        worker.store = FakeWorkerStore()
        client = FakePaymentClient(FakeResponse(200, {"status": "charged"}))

        worker.process_message(
            {"Body": "not-json", "ReceiptHandle": "receipt-001"}, client
        )

        self.assertEqual([], self.queue.deleted)


if __name__ == "__main__":
    unittest.main()
