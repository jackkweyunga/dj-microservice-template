##### Django docker file template

FROM python:3.11-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY . /app

WORKDIR app

# installing dev dependencies
RUN apt-get update \
    && apt-get install -y \
        libpq-dev \
        gcc \
        curl \
        libxml2-dev \
        libxslt-dev \
        libffi-dev \
        libcairo2-dev \
        libpango1.0-dev \
    && apt-get clean \
    && pip3 install --upgrade pip \
    && pip3 install gunicorn \
    && pip3 install psycopg2 \
    && pip3 install --no-cache-dir -r requirements.txt

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/healthcheck/ || exit 1

EXPOSE 8000

CMD python manage.py migrate && \
    daphne -b 0.0.0.0 -p 8000 config.asgi:application

    # when using daphine
    # && daphne -b 0.0.0.0 -p 8000 config.asgi:application
    # using gunicorn
