from django.conf.urls.defaults import *
from django.conf import settings

# Admin
from django.contrib import admin
admin.autodiscover()

# Modules
urlpatterns = patterns('',
    (r'', include('lending.apps.core.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# Medias
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$',
        'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        },
    ),
)