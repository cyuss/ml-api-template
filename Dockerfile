FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /usr/src/tmp
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
poetry lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY app/ ./
EXPOSE 5000

CMD ['uvicorn', 'app.app:app', '--host', '0.0.0.0', '--port', '5000']