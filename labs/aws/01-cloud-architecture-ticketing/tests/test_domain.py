from __future__ import annotations

import pathlib
import sys
import unittest
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

APP_ROOT = pathlib.Path(__file__).resolve().parents[1] / "app"
sys.path.insert(0, str(APP_ROOT))

from ticketing.domain import (  # noqa: E402
    IdempotencyConflict,
    InMemoryTicketing,
    ReservationRequest,
    SeatUnavailable,
)


class TicketingInvariantTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = InMemoryTicketing(hold_seconds=2)
        self.store.add_seat("event-001", "seat-001")
        self.store.add_seat("event-001", "seat-002")

    def test_two_callers_cannot_hold_the_same_seat(self) -> None:
        barrier = Barrier(2)

        def attempt(key: str) -> bool:
            barrier.wait()
            try:
                self.store.reserve(
                    ReservationRequest("event-001", "seat-001"), key, now=100
                )
                return True
            except SeatUnavailable:
                return False

        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(attempt, ["request-a", "request-b"]))

        self.assertEqual(1, sum(results))

    def test_same_idempotency_key_replays_original_result(self) -> None:
        request = ReservationRequest("event-001", "seat-001")
        first, first_replay = self.store.reserve(request, "request-a", now=100)
        second, second_replay = self.store.reserve(request, "request-a", now=101)

        self.assertFalse(first_replay)
        self.assertTrue(second_replay)
        self.assertEqual(first["order_id"], second["order_id"])

    def test_reusing_key_for_different_request_is_rejected(self) -> None:
        self.store.reserve(
            ReservationRequest("event-001", "seat-001"), "request-a", now=100
        )

        with self.assertRaises(IdempotencyConflict):
            self.store.reserve(
                ReservationRequest("event-001", "seat-002"), "request-a", now=101
            )

    def test_expired_hold_can_be_reclaimed(self) -> None:
        first, _ = self.store.reserve(
            ReservationRequest("event-001", "seat-001"), "request-a", now=100
        )
        second, _ = self.store.reserve(
            ReservationRequest("event-001", "seat-001"), "request-b", now=103
        )

        self.assertNotEqual(first["order_id"], second["order_id"])

    def test_dispatch_remains_pending_until_acknowledged(self) -> None:
        order, _ = self.store.reserve(
            ReservationRequest("event-001", "seat-001"), "request-a", now=100
        )

        self.assertEqual(
            [order["order_id"]],
            [o["order_id"] for o in self.store.pending_dispatches()],
        )
        self.store.mark_dispatched(order["order_id"])
        self.assertEqual([], self.store.pending_dispatches())

    def test_unknown_payment_is_reconciled_without_duplicate_confirmation(self) -> None:
        order, _ = self.store.reserve(
            ReservationRequest("event-001", "seat-001", "unknown"),
            "request-a",
            now=100,
        )
        self.store.mark_reconciliation(order["order_id"])
        self.assertEqual(
            "RECONCILIATION", self.store.get_order(order["order_id"])["status"]
        )

        self.store.confirm(order["order_id"])
        self.store.confirm(order["order_id"])
        self.assertEqual("CONFIRMED", self.store.get_order(order["order_id"])["status"])

    def test_decline_releases_the_seat(self) -> None:
        order, _ = self.store.reserve(
            ReservationRequest("event-001", "seat-001", "decline"),
            "request-a",
            now=100,
        )
        self.store.decline(order["order_id"])
        replacement, _ = self.store.reserve(
            ReservationRequest("event-001", "seat-001"), "request-b", now=101
        )
        self.assertNotEqual(order["order_id"], replacement["order_id"])


if __name__ == "__main__":
    unittest.main()
