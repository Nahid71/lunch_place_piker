#!/usr/bin/env bash

# Run in python env

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux OS Found!
    echo yes | python manage.py reset_db -c
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
else
    # Windows OS Found!
    # Do not engage!
    python win_file_mgmt.py --setupdatabase yes
    echo yes | python manage.py reset_db -c
    python win_file_mgmt.py --setupdatabase no
fi

python manage.py makemigrations
python manage.py migrate

python manage.py loaddata user/fixtures/myuser.json
python manage.py loaddata restaurant/fixtures/my_restaurant.json
