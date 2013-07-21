from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mechofduty.gamer.views',
    url(r'^register/$', 'register', name='register'),
    url(r'^register/(?P<user_id>\d)/$', 'register_gamer', name='register_creategamer'),
)
