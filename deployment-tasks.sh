#! /bin/bash

python reseller_cashback/manage.py collectstatic --noinput --clear
python reseller_cashback/manage.py migrate --noinput