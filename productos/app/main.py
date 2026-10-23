import os

from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="Servicio de Productos")
engine = create_engine(os.environ["DATABASE_URL"])


@app.get("/productos/health")
def health():
    with engine.connect() as c:
        c.execute(text("SELECT 1"))
    return {"status": "ok"}


@app.get("/productos")
def listar_productos():
    return [{"id": 1, "nombre": "Teclado"}]
