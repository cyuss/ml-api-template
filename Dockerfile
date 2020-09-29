FROM python:3.8-slim

# set work directory
WORKDIR /usr/src/tmp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV	PYTHONUNBUFFERED 1
ENV	PIP_NO_CACHE_DIR=off
ENV	PIP_DISABLE_PIP_VERSION_CHECK=on
ENV	POETRY_VIRTUALENVS_IN_PROJECT=true
ENV	POETRY_NO_INTERACTION=1

# install poetry
RUN pip install poetry

COPY pyproject.toml ./
RUN poetry install --no-dev

COPY ./app ./app
EXPOSE 5000

CMD poetry run uvicorn app.main:app --host 0.0.0.0 --port 5000