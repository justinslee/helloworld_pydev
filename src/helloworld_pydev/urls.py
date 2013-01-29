from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello_polls/$', 'hello_polls.views.index'),
    url(r'^hello_polls/(?P<poll_id>\d+)/$', 'hello_polls.views.detail'),
    url(r'^hello_polls/(?P<poll_id>\d+)/results/$', 'hello_polls.views.results'),
    url(r'^hello_polls/(?P<poll_id>\d+)/vote/$', 'hello_polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),

)
