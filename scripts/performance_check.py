import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from statistics import mean
from fastapi.testclient import TestClient
from app.main import app

with TestClient(app) as client:
    client.post('/reset', headers={'X-Role': 'ADMIN'})
    client.post('/cases', headers={'X-Role': 'CLERK'}, json={'case_number': '90000-2026', 'subject': 'Performance'})
    durations = []
    for _ in range(100):
        start = time.perf_counter()
        response = client.get('/cases/90000-2026', headers={'X-Role': 'CLERK'})
        durations.append((time.perf_counter() - start) * 1000)
        assert response.status_code == 200
print(f"requests=100 avg_ms={mean(durations):.3f} min_ms={min(durations):.3f} max_ms={max(durations):.3f}")
