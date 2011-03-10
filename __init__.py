# -*- coding: utf-8 -*-

from django.conf import settings
from mongoengine import *

# Connexion
connect(
    settings.DB_NAME,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    username=settings.DB_LOGIN,
    password=settings.DB_PASS
)

#connect('lending', host='flame.mongohq.com', port=27021, username='valentin_lending', password='mongolending')
