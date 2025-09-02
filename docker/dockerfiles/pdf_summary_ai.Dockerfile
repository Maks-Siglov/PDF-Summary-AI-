FROM python:3.12 AS base

WORKDIR /opt/pdf-summary-ai

RUN pip install poetry

COPY poetry.lock pyproject.toml /opt/pdf-summary-ai/

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY src /opt/pdf-summary-ai/src
COPY .env /opt/pdf-summary-ai/.env
COPY entrypoints/prod_entrypoint.sh /opt/pdf-summary-ai/entrypoint.sh


FROM base AS prod

# Gunicorn
EXPOSE 8080

ENTRYPOINT ["sh", "/opt/pdf-summary-ai/entrypoint.sh"]