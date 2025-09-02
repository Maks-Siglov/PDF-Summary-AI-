#!/bin/sh

# Set defaults if env variables are missing
: "${GUNICORN_WORKERS:=1}"
: "${GUNICORN_LOG_LEVEL:=info}"
: "${GUNICORN_PORT:=8080}"
: "${GUNICORN_TIMEOUT:=60}"

echo "Starting PDF Summary AI with Gunicorn..."
echo "Workers: $GUNICORN_WORKERS"
echo "Port: $GUNICORN_PORT"
echo "Log Level: $GUNICORN_LOG_LEVEL"

gunicorn -k uvicorn.workers.UvicornWorker \
        --workers $GUNICORN_WORKERS \
        --log-level $GUNICORN_LOG_LEVEL \
        --bind :$GUNICORN_PORT\
        --log-file - \
        --access-logfile - \
        --error-logfile - \
        --keep-alive 120 \
        --timeout $GUNICORN_TIMEOUT \
        src.main:app