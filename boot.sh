#!/bin/sh
source venv/bin/activate
exec gunicorn -b :80 --access-logfile - --error-logfile - main:app