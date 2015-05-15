from django.conf.urls import patterns, url
from django.views.generic import ListView
from views import indexView, recountInsc, teamDetail, viewCalendar

urlpatterns = patterns('',
	url(r'^$', indexView.as_view()),
	#url(r'^register','competition.views.nuevo_usuario'),
	url(r'^login','competition.views.loginUser'),
	url(r'^privado','competition.views.privado'),
	url(r'^cerrar','competition.views.cerrar'),
	url(r'^teamregister','competition.views.nuevo_equipo_jugador'),
	#url(r'^playerregister','competition.views.nuevo_jugador'),
	url(r'^recount',recountInsc.as_view()),
	url(r'^team/(?P<pk>\d+)/$', teamDetail.as_view(),name='team_detail'),
	url(r'^jugadors','competition.views.inscrits'),
	url(r'^enviarmisatge','competition.views.enviarInfo'),
	url(r'^team/(?P<pk>\d+)/validate','competition.views.validate', name='validate_team'),
	#url(r'^validate','competition.views.Comprovacio'),
	url(r'^generar','competition.views.generarHoraris'),
	url(r'^edit','competition.views.editPlayers'),
	url(r'^calendar', viewCalendar.as_view()),
	url(r'^team/(?P<pk>\d+)\.(?P<extension>(json|xml))$', teamDetail.as_view(),name='team_detail'),
)
