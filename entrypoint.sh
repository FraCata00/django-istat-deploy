#!/bin/sh
echo "Applying migrations..."
python manage.py migrate --noinput

# 2. Import ISTAT
if [ ! -f /app/.istat_imported ]; then
    echo "Importing ISTAT data..."
    python manage.py import_istat_data --force
    touch /app/.istat_imported
else
    echo "ISTAT data already imported, skipping..."
fi

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
