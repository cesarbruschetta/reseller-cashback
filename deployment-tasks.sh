#! /bin/bash

python reseller_cashback/manage.py collectstatic --noinput
python reseller_cashback/manage.py migrate --noinput