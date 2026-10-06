"""Environment-based configuration for the local lab."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    region: str = os.getenv("AWS_REGION", "us-east-1")
    dynamodb_endpoint: str = os.getenv("DYNAMODB_ENDPOINT", "http://dynamodb:8000")
    sqs_endpoint: str = os.getenv("QUEUE_ENDPOINT", "http://localstack:4566")
    inventory_table: str = os.getenv("INVENTORY_TABLE", "ticketing-inventory")
    orders_table: str = os.getenv("ORDERS_TABLE", "ticketing-orders")
    idempotency_table: str = os.getenv("IDEMPOTENCY_TABLE", "ticketing-idempotency")
    queue_name: str = os.getenv("QUEUE_NAME", "ticketing-orders")
    dlq_name: str = os.getenv("DLQ_NAME", "ticketing-orders-dlq")
    payment_url: str = os.getenv("PAYMENT_STUB_URL", "http://payment-stub:8081")
    hold_seconds: int = int(os.getenv("RESERVATION_HOLD_SECONDS", "120"))
    payment_timeout_seconds: float = float(os.getenv("PAYMENT_TIMEOUT_SECONDS", "2"))
    worker_wait_seconds: int = int(os.getenv("WORKER_WAIT_SECONDS", "5"))


settings = Settings()
