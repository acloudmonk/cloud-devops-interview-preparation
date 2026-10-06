"""HTTP API for browsing, reserving, and observing local lab orders."""

from __future__ import annotations

import logging
from typing import Literal

from fastapi import FastAPI, Header, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict, Field

from .adapters import DynamoTicketStore, SqsOrderQueue
from .config import settings
from .domain import IdempotencyConflict, ReservationRequest, SeatUnavailable

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger("ticketing.api")

app = FastAPI(title="Ticketing Lab API", version="0.1.0")
store = DynamoTicketStore(settings)
queue = SqsOrderQueue(settings)


class ReservationBody(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    event_id: str = Field(alias="eventId", min_length=1, max_length=100)
    seat_id: str = Field(alias="seatId", min_length=1, max_length=100)
    payment_mode: Literal["success", "decline", "timeout", "unknown"] = Field(
        default="success", alias="paymentMode"
    )


def _public_order(order: dict, replayed: bool = False) -> dict:
    return {
        "orderId": order["order_id"],
        "eventId": order["event_id"],
        "seatId": order["seat_id"],
        "status": order["status"],
        "dispatchStatus": order["dispatch_status"],
        "holdExpiresAt": int(order["hold_expires_at"]),
        "replayed": replayed,
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict[str, str]:
    try:
        if not store.ready() or not queue.ready():
            raise RuntimeError("local dependencies are not initialized")
    except Exception as error:
        raise HTTPException(
            status_code=503, detail="dependencies unavailable"
        ) from error
    return {"status": "ready"}


@app.get("/events/{event_id}")
def get_event(event_id: str) -> dict:
    try:
        return store.get_event(event_id)
    except KeyError as error:
        raise HTTPException(status_code=404, detail="event not found") from error


@app.post("/reservations", status_code=status.HTTP_202_ACCEPTED)
def create_reservation(
    body: ReservationBody,
    response: Response,
    idempotency_key: str = Header(
        alias="Idempotency-Key", min_length=8, max_length=128
    ),
) -> dict:
    request = ReservationRequest(
        event_id=body.event_id,
        seat_id=body.seat_id,
        payment_mode=body.payment_mode,
    )
    try:
        order, replayed = store.reserve(request, idempotency_key)
    except IdempotencyConflict as error:
        raise HTTPException(status_code=409, detail=str(error)) from error
    except SeatUnavailable as error:
        raise HTTPException(status_code=409, detail=str(error)) from error

    if order["dispatch_status"] == "PENDING":
        try:
            queue.publish(order["order_id"])
            store.mark_dispatched(order["order_id"])
            order["dispatch_status"] = "SENT"
        except Exception:
            logger.exception("order dispatch deferred order_id=%s", order["order_id"])

    if replayed:
        response.status_code = status.HTTP_200_OK
    return _public_order(order, replayed=replayed)


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> dict:
    order = store.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="order not found")
    return _public_order(order)
