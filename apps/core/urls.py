# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from lending.apps.core.views import *

# Règles
urlpatterns = patterns('',
    (r'^$', home),
    (r'^login/$', login)
)