#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate

gunicorn Libracours.wsgi:application \
    --name Libracours \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --access-logfile - \
    --error-logfile -
