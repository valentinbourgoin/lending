# -*- coding: utf-8 -*-

import os.path
from django.utils.translation import gettext_lazy as _

# Debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Valentin', 'valentin.bourgoin@gmail.com'),
)
MANAGERS = ADMINS

# Bases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lending',
        'USER': 'root',
        'PASSWORD': '',            
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Langues
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
LANGUAGES = (
  ('fr', _('Français')),
)
DEFAULT_LANGUAGE = 1

# Paths
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'bw2f9_+ljl85rth@&tl%n-w1v%5&s9$1^l9*4k&)bqc=nfpxg!'

# Middlewares
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# URLs
ROOT_URLCONF = 'lending.urls'

# Templates
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)
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

# Apps
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

# Auth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'mongoengine.django.auth.MongoEngineBackend',
    'lending.apps.core.auth_backend.CoreUserModelBackend',
)
LOGIN_REDIRECT_URL = '/'
SESSION_ENGINE = 'mongoengine.django.sessions'

# MongoDB
DB_NAME = 'lending'
DB_HOST = 'localhost'
DB_PORT = 27017
DB_LOGIN = ''
DB_PASS = ''