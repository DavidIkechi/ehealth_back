#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create a superuser
# Set environment variables for the superuser in Vercel or handle securely
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
if not User.objects.filter(username='admin').exists(): \
    User.objects.create_superuser('katie_admin', 'akwuru.david@ul.ie', 'ehealth_hub@123£')" | python manage.py shell

# Collect static files
python manage.py collectstatic --noinput

# Create a build directory if it doesn't exist
mkdir -p build

# Move necessary files into the build directory
cp -r staticfiles build/
cp -r your_project_name build/
cp manage.py build/
