import os

from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="Servicio de Usuarios")
engine = create_engine(os.environ["DATABASE_URL"])


@app.get("/usuarios/health")
def health():
    with engine.connect() as c:
        c.execute(text("SELECT 1"))
    return {"status": "ok"}


@app.get("/usuarios")
def listar_usuarios():
    return [{"id": 1, "nombre": "Ana"}]
