# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from lending.apps.core.views import *

# R�gles
urlpatterns = patterns('',
    (r'^$', home),
    (r'^login/$', login)
)