FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./shop /app

RUN python manage.py collectstatic --noinput

ENTRYPOINT python manage.py migrate && \
           python manage.py loaddata mock_data/products.json || true && \
           gunicorn --bind 0.0.0.0:8000 shop.wsgi:application
