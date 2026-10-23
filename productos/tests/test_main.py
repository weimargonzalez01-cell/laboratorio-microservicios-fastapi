from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/productos/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_listar():
    r = client.get("/productos")
    assert r.status_code == 200
    assert r.json()[0]["nombre"] == "Teclado"
