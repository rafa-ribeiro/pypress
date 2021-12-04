#!/usr/bin/env bash

echo "Starting UI TestRunner..."
gunicorn --reload pypress.app --bind 0.0.0.0:8000 --timeout 30 --workers 3

# no reload
#gunicorn pypress.app --bind 0.0.0.0:8000 --timeout 30 --workers 3