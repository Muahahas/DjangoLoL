from django.conf.urls import patterns, url
from django.views.generic import ListView
from views import indexView

urlpatterns = patterns('',
	url(r'^$', indexView.as_view()),
	url(r'^register','competition.views.nuevo_usuario'),
	url(r'^login','competition.views.loginUser'),
	url(r'^privado','competition.views.privado'),
	url(r'^cerrar','competition.views.cerrar'),
	url(r'^teamregister','competition.views.nuevo_equipo'),
)