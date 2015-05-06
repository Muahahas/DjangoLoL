from django.conf.urls import patterns, url
from django.views.generic import ListView
from views import indexView

urlpatterns = patterns('',
	url(r'^$', indexView.as_view()),
	url(r'^usuario/nuevo$','competition.views.nuevo_usuario'),
	url(r'^login','competition.views.loginUser'),
)