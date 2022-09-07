#!/bin/bash
set -eo pipefail

#locate manage.py
if [[ ! -f "manage.py" ]]
then
   ln -s ./src/manage.py .
fi

#add logs directory
if [[ ! -d "./logs" ]]
then
    mkdir -p ./logs
fi
# Create migrations
python3 manage.py makemigrations

# Run migrations
python3 manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run supervisord
/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf

exit 0
