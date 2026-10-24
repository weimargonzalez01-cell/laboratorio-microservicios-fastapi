# Requisitos de calidad

Aquí se muestra qué pedía el laboratorio, cómo se midió y qué resultado dio.

| Aspecto | Qué se pide | Cómo se mide | Resultado |
|---|---|---|---|
| Estilo del código | Código limpio y ordenado | Ruff (`ruff check .` y `ruff format --check .`) | 0 errores en los 3 servicios |
| Pruebas | Cobertura de al menos 80 % | pytest (`pytest --cov=app --cov-fail-under=80`) | 100 % en los 3 servicios |
| Seguridad del código | Sin hallazgos de seguridad | Bandit (`bandit -r app`) | 0 hallazgos en los 3 servicios |
| Red privada | Las bases de datos no se alcanzan desde el equipo | `Test-NetConnection localhost -Port 5432` | `False`, el puerto está cerrado |
| Rendimiento | Responder en 2 segundos o menos con 100 usuarios | Locust (100 usuarios, 30 segundos) | Promedio 5.19 ms, máximo 192 ms, 0 fallos en 2519 peticiones |

## Evidencias

- Ruff, pytest y Bandit: carpeta `entregables/4-evidencias/calidad/` (archivos 06, 07 y 08 de cada servicio).
- Red privada: carpeta `entregables/4-evidencias/seguridad/`.
- Locust: `entregables/4-evidencias/calidad/09-locust.png` y el reporte completo `locust.html`.