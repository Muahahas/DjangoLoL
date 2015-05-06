from django.conf.urls import patterns, url
from django.views.generic import ListView
from views import indexView

urlpatterns = patterns('',
	url(r'^$', indexView.as_view()),
)