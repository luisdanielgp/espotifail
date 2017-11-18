from .base import *
import os


SECRET_KEY = 'kn@)%zw#6p+^whw-$=y)g^@)+r48dlcq6=dmp6yy8!k46sa@k*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'espotifail',
        'USER': 'admin_espotifail',
        'PASSWORD': 'admin_espotifail',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

STATICFILES_DIRS = [os.path.join(os.getcwd(), "static")]
