# Homework 5 — API de predicción

Archivos copiados del entorno de referencia de 2026:
`machine-learning-zoomcamp/cohorts/2026/homework/05-deployment/`.

`predict.py` carga `pipeline.bin` y define `GET /health` y `POST /predict`.
`model.py` aplica los valores predeterminados de `feature_defaults.json`.
Este directorio tiene su propio `pyproject.toml` y `uv.lock`, con Python 3.11
y Scikit-Learn 1.7.2.

Desde la raíz de `machine-learning-zoomcamp-homework`:

```bash
cd 05-deployment
uv sync --locked
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

Si ya hay un servidor en el puerto 9696, detén ese proceso antes de iniciar
esta copia.

En otra terminal:

```bash
curl -s http://localhost:9696/health

curl -s http://localhost:9696/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74
  }'
```

Respuesta verificada con la API original y este mismo modelo:

```json
{"conversion_probability": 0.769799, "conversion": true}
```

Respuesta de Question 4 redondeada a tres decimales: **0.770**.
