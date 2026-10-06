"""Smoke test for an already running local Compose stack."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request

BASE_URL = "http://localhost:8080"
IDEMPOTENCY_KEY = "smoke-event-001-seat-001"


def request(method: str, path: str, body: dict | None = None, headers=None) -> dict:
    data = None if body is None else json.dumps(body).encode("utf-8")
    request_headers = {"Content-Type": "application/json", **(headers or {})}
    operation = urllib.request.Request(
        f"{BASE_URL}{path}", data=data, headers=request_headers, method=method
    )
    try:
        with urllib.request.urlopen(operation, timeout=5) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8")
        raise RuntimeError(f"{method} {path} failed: {error.code} {detail}") from error


def main() -> None:
    ready = request("GET", "/ready")
    assert ready["status"] == "ready"

    payload = {
        "eventId": "event-001",
        "seatId": "seat-001",
        "paymentMode": "success",
    }
    first = request(
        "POST",
        "/reservations",
        payload,
        {"Idempotency-Key": IDEMPOTENCY_KEY},
    )
    replay = request(
        "POST",
        "/reservations",
        payload,
        {"Idempotency-Key": IDEMPOTENCY_KEY},
    )
    assert first["orderId"] == replay["orderId"]
    assert replay["replayed"] is True

    order = first
    for _ in range(15):
        order = request("GET", f"/orders/{first['orderId']}")
        if order["status"] == "CONFIRMED":
            break
        time.sleep(1)
    assert order["status"] == "CONFIRMED", order
    print(json.dumps({"smoke": "passed", "order": order}, indent=2))


if __name__ == "__main__":
    main()
