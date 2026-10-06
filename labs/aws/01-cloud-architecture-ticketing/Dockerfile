FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements-app.txt ./
RUN python -m pip install --no-cache-dir --requirement requirements-app.txt \
    && addgroup --system --gid 10001 app \
    && adduser --system --uid 10001 --gid 10001 app

COPY app/ ./

USER 10001:10001

EXPOSE 8080

CMD ["uvicorn", "ticketing.api:app", "--host", "0.0.0.0", "--port", "8080"]
