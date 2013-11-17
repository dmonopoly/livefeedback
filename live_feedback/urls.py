from django.conf.urls import patterns, url

from live_feedback import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^vote/$', views.vote, name='vote'),
)
