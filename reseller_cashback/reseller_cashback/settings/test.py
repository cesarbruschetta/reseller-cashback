# flake8: noqa

from reseller_cashback.settings.base import *


LANGUAGE_CODE = 'en'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
HOST_PROTOCOL = 'http'
