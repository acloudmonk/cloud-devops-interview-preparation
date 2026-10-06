"""Business invariants independent of HTTP, DynamoDB, and SQS."""

from __future__ import annotations

import hashlib
import json
import threading
import time
import uuid
from copy import deepcopy
from dataclasses import dataclass


class TicketingError(Exception):
    """Base class for expected business errors."""


class SeatUnavailable(TicketingError):
    """The requested seat cannot be reserved."""


class IdempotencyConflict(TicketingError):
    """An idempotency key was reused for a different request."""


class OrderNotFound(TicketingError):
    """The requested order does not exist."""


@dataclass(frozen=True)
class ReservationRequest:
    event_id: str
    seat_id: str
    payment_mode: str = "success"

    @property
    def fingerprint(self) -> str:
        payload = {
            "event_id": self.event_id,
            "payment_mode": self.payment_mode,
            "seat_id": self.seat_id,
        }
        encoded = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


class InMemoryTicketing:
    """Thread-safe model used to prove the lab's correctness invariants."""

    def __init__(self, hold_seconds: int = 120) -> None:
        self.hold_seconds = hold_seconds
        self._lock = threading.RLock()
        self._seats: dict[str, dict] = {}
        self._orders: dict[str, dict] = {}
        self._idempotency: dict[str, dict] = {}

    @staticmethod
    def seat_key(event_id: str, seat_id: str) -> str:
        return f"{event_id}#{seat_id}"

    def add_seat(self, event_id: str, seat_id: str) -> None:
        key = self.seat_key(event_id, seat_id)
        with self._lock:
            self._seats[key] = {
                "event_id": event_id,
                "seat_id": seat_id,
                "state": "AVAILABLE",
            }

    def reserve(
        self,
        request: ReservationRequest,
        idempotency_key: str,
        now: int | None = None,
    ) -> tuple[dict, bool]:
        timestamp = int(time.time()) if now is None else now
        with self._lock:
            previous = self._idempotency.get(idempotency_key)
            if previous:
                if previous["fingerprint"] != request.fingerprint:
                    raise IdempotencyConflict(
                        "idempotency key belongs to a different request"
                    )
                return deepcopy(self._orders[previous["order_id"]]), True

            seat_key = self.seat_key(request.event_id, request.seat_id)
            seat = self._seats.get(seat_key)
            if seat is None:
                raise SeatUnavailable("seat does not exist")

            if seat["state"] == "HELD" and seat.get("hold_expires_at", 0) <= timestamp:
                seat.clear()
                seat.update(
                    {
                        "event_id": request.event_id,
                        "seat_id": request.seat_id,
                        "state": "AVAILABLE",
                    }
                )

            if seat["state"] != "AVAILABLE":
                raise SeatUnavailable("seat is already held or confirmed")

            order_id = str(uuid.uuid4())
            expires_at = timestamp + self.hold_seconds
            seat.update(
                {
                    "state": "HELD",
                    "order_id": order_id,
                    "hold_expires_at": expires_at,
                }
            )
            order = {
                "order_id": order_id,
                "event_id": request.event_id,
                "seat_id": request.seat_id,
                "status": "RESERVED",
                "payment_mode": request.payment_mode,
                "dispatch_status": "PENDING",
                "hold_expires_at": expires_at,
                "created_at": timestamp,
            }
            self._orders[order_id] = order
            self._idempotency[idempotency_key] = {
                "fingerprint": request.fingerprint,
                "order_id": order_id,
            }
            return deepcopy(order), False

    def get_order(self, order_id: str) -> dict:
        with self._lock:
            if order_id not in self._orders:
                raise OrderNotFound(order_id)
            return deepcopy(self._orders[order_id])

    def mark_dispatched(self, order_id: str) -> None:
        with self._lock:
            self._require_order(order_id)["dispatch_status"] = "SENT"

    def mark_reconciliation(self, order_id: str) -> None:
        with self._lock:
            order = self._require_order(order_id)
            if order["status"] not in {"CONFIRMED", "DECLINED"}:
                order["status"] = "RECONCILIATION"

    def confirm(self, order_id: str) -> None:
        with self._lock:
            order = self._require_order(order_id)
            if order["status"] == "CONFIRMED":
                return
            seat = self._seats[self.seat_key(order["event_id"], order["seat_id"])]
            if seat.get("order_id") != order_id:
                raise SeatUnavailable("reservation ownership changed")
            seat["state"] = "CONFIRMED"
            order["status"] = "CONFIRMED"

    def decline(self, order_id: str) -> None:
        with self._lock:
            order = self._require_order(order_id)
            if order["status"] == "DECLINED":
                return
            if order["status"] == "CONFIRMED":
                raise TicketingError("a confirmed order cannot be declined")
            seat = self._seats[self.seat_key(order["event_id"], order["seat_id"])]
            if seat.get("order_id") == order_id:
                seat.clear()
                seat.update(
                    {
                        "event_id": order["event_id"],
                        "seat_id": order["seat_id"],
                        "state": "AVAILABLE",
                    }
                )
            order["status"] = "DECLINED"

    def pending_dispatches(self) -> list[dict]:
        with self._lock:
            return [
                deepcopy(order)
                for order in self._orders.values()
                if order["dispatch_status"] == "PENDING"
                and order["status"] not in {"CONFIRMED", "DECLINED"}
            ]

    def _require_order(self, order_id: str) -> dict:
        order = self._orders.get(order_id)
        if order is None:
            raise OrderNotFound(order_id)
        return order
