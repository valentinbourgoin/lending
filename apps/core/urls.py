# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from lending.apps.core.views import *

# Règles
urlpatterns = patterns('',
    (r'^$', home),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
)