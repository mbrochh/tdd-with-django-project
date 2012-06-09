"""Global URLs file that defines which app is available under which URL."""
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jasmine/', include('django_jasmine.urls')),
    url(r'^', include('myapp.urls')),
)
