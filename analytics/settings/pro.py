from .base import *

DEBUG = False
ADMINS = (
    ('Phan Quốc Lân', 'greenmails2001@gmail.com'),
)
ALLOWED_HOSTS = ['pmdata.vn', 'www.pmdata.vn']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'budgetdb',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'zxcasdqwe',                  # Not used with sqlite3.
        'HOST': '192.168.1.177',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}