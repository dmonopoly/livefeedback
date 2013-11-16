from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
#     url(r'^$', include('live_feedback.urls')),
    url(r'^live_feedback/', include('live_feedback.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
