#!/bin/bash

python3 manage.py makemigrations && python3 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.all().delete()" | ./manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', ' admin@admin.com ', 'admin')" | ./manage.py shell

python3 manage.py runserver 0.0.0.0:8000