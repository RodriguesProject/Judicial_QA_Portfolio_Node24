import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        c.post('/reset', headers={'X-Role': 'ADMIN'})
        yield c
        c.post('/reset', headers={'X-Role': 'ADMIN'})
