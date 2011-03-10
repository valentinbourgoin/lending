# -*- coding: utf-8 -*-

from mongoengine import *

from lending.apps.core.models import Item

class Author(Document):
    name     = StringField(required=True)
    forename = StringField(required=True)

    def __unicode__(self):
        return u'%s %s' % (self.forename, self.name)

class Family(Document):
    name     = StringField(required=True)
    slug     = StringField(required=True)

    def __unicode__(self):
        return u'%s' % self.name

class Category(Document):
    name     = StringField(required=True)
    slug     = StringField(required=True)
    family   = ReferenceField(Family, required=True)

    def __unicode__(self):
        return u'%s' % self.name

class Book(Item):
    cover        = URLField()
    description  = StringField()
    author       = ReferenceField(Author)
    categories   = ListField(ReferenceField(Category))

    def __unicode__(self):
        return u'%s' % self.title
