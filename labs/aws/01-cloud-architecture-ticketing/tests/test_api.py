from __future__ import annotations

import os
import pathlib
import sys
import unittest

os.environ.setdefault("AWS_ACCESS_KEY_ID", "local")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "local")
os.environ.setdefault("AWS_EC2_METADATA_DISABLED", "true")

APP_ROOT = pathlib.Path(__file__).resolve().parents[1] / "app"
sys.path.insert(0, str(APP_ROOT))

from fastapi.testclient import TestClient  # noqa: E402
from ticketing import api, payment_stub  # noqa: E402
from ticketing.domain import InMemoryTicketing  # noqa: E402


class FakeStore:
    def __init__(self) -> None:
        self.model = InMemoryTicketing()
        self.model.add_seat("event-001", "seat-001")
        self.model.add_seat("event-001", "seat-002")

    def ready(self) -> bool:
        return True

    def get_event(self, event_id: str) -> dict:
        if event_id != "event-001":
            raise KeyError(event_id)
        return {"eventId": event_id, "seatCount": 2, "availableCount": 2}

    def reserve(self, request, idempotency_key: str):
        return self.model.reserve(request, idempotency_key)

    def mark_dispatched(self, order_id: str) -> None:
        self.model.mark_dispatched(order_id)

    def get_order(self, order_id: str):
        try:
            return self.model.get_order(order_id)
        except Exception:
            return None


class FakeQueue:
    def __init__(self) -> None:
        self.published: list[str] = []

    def ready(self) -> bool:
        return True

    def publish(self, order_id: str) -> str:
        self.published.append(order_id)
        return "message-001"


class ApiContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = FakeStore()
        self.queue = FakeQueue()
        api.store = self.store
        api.queue = self.queue
        self.client = TestClient(api.app)

    def test_reservation_is_accepted_and_replay_is_safe(self) -> None:
        payload = {"eventId": "event-001", "seatId": "seat-001"}
        headers = {"Idempotency-Key": "contract-request-001"}

        first = self.client.post("/reservations", json=payload, headers=headers)
        replay = self.client.post("/reservations", json=payload, headers=headers)

        self.assertEqual(202, first.status_code)
        self.assertEqual(200, replay.status_code)
        self.assertEqual(first.json()["orderId"], replay.json()["orderId"])
        self.assertTrue(replay.json()["replayed"])
        self.assertEqual(1, len(self.queue.published))

    def test_same_key_with_different_payload_conflicts(self) -> None:
        headers = {"Idempotency-Key": "contract-request-001"}
        self.client.post(
            "/reservations",
            json={"eventId": "event-001", "seatId": "seat-001"},
            headers=headers,
        )

        response = self.client.post(
            "/reservations",
            json={"eventId": "event-001", "seatId": "seat-002"},
            headers=headers,
        )

        self.assertEqual(409, response.status_code)

    def test_missing_idempotency_key_is_rejected(self) -> None:
        response = self.client.post(
            "/reservations",
            json={"eventId": "event-001", "seatId": "seat-001"},
        )
        self.assertEqual(422, response.status_code)

    def test_readiness_checks_dependencies(self) -> None:
        response = self.client.get("/ready")
        self.assertEqual({"status": "ready"}, response.json())


class PaymentStubContractTests(unittest.TestCase):
    def setUp(self) -> None:
        payment_stub._payments.clear()
        self.client = TestClient(payment_stub.app)

    def test_unknown_response_can_be_reconciled_without_second_charge(self) -> None:
        headers = {"Idempotency-Key": "payment-order-001"}
        payload = {"order_id": "payment-order-001", "mode": "unknown"}

        response = self.client.post("/payments", json=payload, headers=headers)
        lookup = self.client.get("/payments/payment-order-001")

        self.assertEqual(504, response.status_code)
        self.assertEqual("charged", lookup.json()["status"])


if __name__ == "__main__":
    unittest.main()
