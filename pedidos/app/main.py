import os

from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="Servicio de Pedidos")
engine = create_engine(os.environ["DATABASE_URL"])


@app.get("/pedidos/health")
def health():
    with engine.connect() as c:
        c.execute(text("SELECT 1"))
    return {"status": "ok"}


@app.get("/pedidos")
def listar_pedidos():
    return [{"id": 1, "producto": "Teclado", "cantidad": 2}]
