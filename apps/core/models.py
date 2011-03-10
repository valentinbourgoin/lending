# -*- coding: utf-8 -*-

from django.db import models
from mongoengine import *
from mongoengine.django.auth import User

# Lieu
class Place(Document):
    name  = StringField(required=True)
    lat   = StringField(max_length=50, required=True)
    long  = StringField(max_length=50, required=True)

# Utilisateur
class CoreUser(User):
    birthdate = DateTimeField()
    avatar    = FileField()

    #objects  = UserManager()

# Element
class Item(Document):
    title = StringField(required=True)


