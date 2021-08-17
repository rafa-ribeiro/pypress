#!/usr/bin/env bash

echo "Starting UI TestRunner..."
#gunicorn --reload ui_testrunner.app --bind 0.0.0.0:8000 --timeout 30 --workers 3

# no reload
gunicorn ui_testrunner.app --bind 0.0.0.0:8000 --timeout 30 --workers 3