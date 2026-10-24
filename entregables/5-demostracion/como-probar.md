# Cómo probar el sistema

Los comandos se ejecutan desde la carpeta `laboratorio/`, en PowerShell.

## 1. Levantar el sistema

```
docker compose down
docker compose up --build -d
docker compose ps
```

Deben aparecer los 8 contenedores corriendo.

## 2. Probar los tres servicios

```
curl.exe http://localhost/usuarios
curl.exe http://localhost/productos
curl.exe http://localhost/pedidos
```

Cada uno responde con su lista.

## 3. Probar que cada servicio llega a su base de datos

```
curl.exe http://localhost/usuarios/health
curl.exe http://localhost/productos/health
curl.exe http://localhost/pedidos/health
```

Los tres responden que están bien.

## 4. Mostrar la red privada

```
docker network inspect laboratorio_privada --format "{{.Internal}}"
Test-NetConnection localhost -Port 5432
```

El primero da `True` y el segundo da `False`: las bases de datos no se alcanzan desde el equipo.

## 5. Mostrar la calidad (en un servicio de ejemplo)

```
cd usuarios
.venv\Scripts\activate
ruff check .
pytest --cov=app --cov-fail-under=80
bandit -r app
deactivate
cd ..
```

Ruff sin errores, cobertura de 100 % y Bandit sin hallazgos.

## 6. Mostrar el rendimiento

```
.venv\Scripts\activate
locust --headless -u 100 -r 10 -t 30s -H http://localhost
```

0 fallos y tiempos de pocos milisegundos.