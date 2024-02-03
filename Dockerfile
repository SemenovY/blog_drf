FROM python:3.11-slim

WORKDIR /app

ENV PUTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml .env ./

RUN apt update && pip install --user poetry

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry install
