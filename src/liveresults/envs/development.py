from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
    'debug_toolbar',
]+INSTALLED_APPS

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'liveresults',
        'USER': 'liveresults',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_liveresults',
        },
    }
}