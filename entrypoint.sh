#!/bin/sh
echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Remember to set import istat data"
echo "Use -> python manage.py import_istat_data --force"

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application \
--bind 0.0.0.0:${PORT:-8000} \
--workers 1 \
--worker-class gthread \
--threads 4 \
--max-requests 1000 \
--max-requests-jitter 100 \
--timeout 120 \
--access-logfile - \
--error-logfile -
