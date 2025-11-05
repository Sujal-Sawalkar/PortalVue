#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Build React frontend
cd frontend
npm install
npm run build
cd ..

# Move build files to Django static
mkdir -p backend/static
cp -r frontend/build/* backend/static/

# Collect static files for Django
python backend/manage.py collectstatic --noinput
