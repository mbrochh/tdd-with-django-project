from django.conf.urls import patterns, url

from myapp.views import HomeView, EntryDetailView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^/entries/(?P<pk>\d+)/$', EntryDetailView.as_view(),
        name='entry_detail'),
)
