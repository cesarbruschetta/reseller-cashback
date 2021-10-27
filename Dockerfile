FROM python:3.9.0-slim-buster

# Install.
RUN pip install poetry gunicorn

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    SECRET_KEY="collectstatic" \
    DJANGO_SETTINGS_MODULE=reseller_cashback.settings.production \
    PORT=8000 \
    WEB_CONCURRENCY=3

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD . /app/
RUN python reseller_cashback/manage.py collectstatic --noinput --clear

EXPOSE 8000   

CMD gunicorn --chdir reseller_cashback reseller_cashback.wsgi:application
