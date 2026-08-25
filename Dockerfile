# =========================================
# Base
# =========================================
FROM python:3.12-slim AS base

ENV POETRY_VERSION=2.4.1

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/


# =========================================
# Development
# =========================================
FROM base AS dev

# Install all dependencies, including dev dependencies
RUN poetry install --no-ansi --no-root

COPY getfit/ /app/getfit

EXPOSE 8000

CMD ["uvicorn", "getfit.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# =========================================
# Production Builder
# =========================================
FROM base AS builder

# Install production dependencies only
RUN poetry install --no-ansi --only main --no-root


# =========================================
# Production
# =========================================
FROM python:3.12-slim AS prod

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy installed Python packages
COPY --from=builder /usr/local /usr/local

# Copy application
COPY getfit/ /app/getfit

EXPOSE 8000

CMD ["gunicorn", "getfit.main:app", "-k", "uvicorn_worker.UvicornWorker", "--bind", "0.0.0.0:8000", "--workers", "2"]