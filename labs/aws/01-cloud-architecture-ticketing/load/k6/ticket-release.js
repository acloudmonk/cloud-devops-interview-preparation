import http from 'k6/http';
import { check, sleep } from 'k6';

const baseUrl = __ENV.BASE_URL;
const eventId = __ENV.EVENT_ID || 'event-001';

if (!baseUrl) {
  throw new Error('BASE_URL is required; use only an authorized lab endpoint');
}

export const options = {
  scenarios: {
    baseline: {
      executor: 'ramping-vus',
      startVUs: 1,
      stages: [
        { duration: '30s', target: 5 },
        { duration: '2m', target: 5 },
        { duration: '30s', target: 0 },
      ],
      gracefulRampDown: '30s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<2000'],
    checks: ['rate>0.99'],
  },
};

export default function () {
  const browse = http.get(`${baseUrl}/events/${eventId}`);
  check(browse, {
    'browse succeeds': (response) => response.status === 200,
  });

  const idempotencyKey = `k6-${__VU}-${__ITER}-${Date.now()}`;
  const reservation = http.post(
    `${baseUrl}/reservations`,
    JSON.stringify({ eventId, seatId: `seat-${__VU}-${__ITER}` }),
    {
      headers: {
        'Content-Type': 'application/json',
        'Idempotency-Key': idempotencyKey,
      },
    },
  );

  check(reservation, {
    'reservation accepted or safely conflicts': (response) =>
      [200, 201, 202, 409].includes(response.status),
  });

  sleep(1);
}
