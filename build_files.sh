#!/bin/bash

# Install dependencies
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

# Install project dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Migrate database
python3 manage.py makemigrations
python3 manage.py migrate