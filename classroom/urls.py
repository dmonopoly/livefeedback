from django.conf.urls import patterns, include, url
# If X, X = "not using django.contrib.staticfiles"
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
  url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
  url(r'^$', include('live_feedback.urls')),
  url(r'^live_feedback/', include('live_feedback.urls', namespace="live_feedback")),
  url(r'^polls/', include('polls.urls', namespace="polls")),
  url(r'^admin/', include(admin.site.urls)),

)

# If X
# urlpatterns += staticfiles_urlpatterns()
