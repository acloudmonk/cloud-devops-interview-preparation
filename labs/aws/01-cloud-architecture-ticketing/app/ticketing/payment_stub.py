"""Idempotent payment-provider stub with controllable failure modes."""

from __future__ import annotations

import threading
import time
from typing import Any, Literal

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Ticketing Payment Stub", version="0.1.0")
_lock = threading.RLock()
_payments: dict[str, dict[str, str]] = {}


class PaymentRequest(BaseModel):
    order_id: str
    mode: Literal["success", "decline", "timeout", "unknown"] = "success"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/payments")
def create_payment(
    body: PaymentRequest,
    idempotency_key: str = Header(
        alias="Idempotency-Key", min_length=8, max_length=128
    ),
) -> Any:
    with _lock:
        previous = _payments.get(idempotency_key)
        if previous:
            if previous["order_id"] != body.order_id:
                raise HTTPException(
                    status_code=409,
                    detail="payment idempotency key belongs to another order",
                )
            return previous

    if body.mode == "timeout":
        time.sleep(10)
        return {"order_id": body.order_id, "status": "not_charged"}

    result = {
        "order_id": body.order_id,
        "status": "declined" if body.mode == "decline" else "charged",
    }
    with _lock:
        _payments[idempotency_key] = result

    if body.mode == "unknown":
        return JSONResponse(
            status_code=504,
            content={"detail": "charge accepted but response was lost"},
        )
    return result


@app.get("/payments/{idempotency_key}")
def get_payment(idempotency_key: str) -> dict:
    with _lock:
        result = _payments.get(idempotency_key)
    if result is None:
        raise HTTPException(status_code=404, detail="payment not found")
    return result
