#!/bin/bash
cd /btce
python manage.py migrate
python manage.py makemessages
python manage.py compilemessages
python manage.py runserver 0.0.0.0:8000
