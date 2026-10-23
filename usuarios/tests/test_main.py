from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/usuarios/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_listar():
    r = client.get("/usuarios")
    assert r.status_code == 200
    assert r.json()[0]["nombre"] == "Ana"
