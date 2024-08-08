#!/bin/bash

# Activate the venv if not activated
source .venv/bin/activate

# Give user feedback
echo "venv activated. Starting gunicorn..."

# Run the app
gunicorn -w 4 "app.app:create_app"