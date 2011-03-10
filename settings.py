# -*- coding: utf-8 -*-

import os.path
from django.utils.translation import gettext_lazy as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Valentin', 'valentin.bourgoin@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
LANGUAGES = (
  ('fr', _('Français')),
)
DEFAULT_LANGUAGE = 1

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'bw2f9_+ljl85rth@&tl%n-w1v%5&s9$1^l9*4k&)bqc=nfpxg!'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.media",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'lending.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'mongoengine',
    'lending.apps.core',
    'lending.apps.books',
)

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
    #'lending.apps.core.auth_backend.CustomUserModelBackend',
)
CUSTOM_USER_MODEL = 'lending.apps.core.CoreUser'

SESSION_ENGINE = 'mongoengine.django.sessions'

# MongoDB
DB_NAME = 'lending'
DB_HOST = 'localhost'
DB_PORT = 27017
DB_LOGIN = ''
DB_PASS = ''