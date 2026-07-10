# -------- builder (install dependencies) --------
FROM python:3.12-slim AS builder

ENV POETRY_VERSION=2.4.1
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/

# Install only production dependencies
RUN poetry install --no-ansi --only main --no-root

# -------- runtime (smaller image) --------
FROM python:3.12-slim AS runtime

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy installed site-packages and console scripts from builder
# (works for the common /usr/local layout in python:slim images)
COPY --from=builder /usr/local /usr/local

# Copy application code
COPY getfit/ /app/getfit

EXPOSE 8000

# Adjust "main:app" to your FastAPI import path
# Example: app = FastAPI() in main.py -> "main:app"
CMD ["gunicorn","getfit.main:app","-k", "uvicorn_worker.UvicornWorker","--bind", "0.0.0.0:8000","--workers", "2"]