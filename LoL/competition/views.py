from django.shortcuts import render, render_to_response, RequestContext
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from models import *
from forms import *

#imports login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

class indexView(ListView):
	template_name = 'competition/index.html'
	queryset=Equip.objects.all()

#No s'utilitza
def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('competition/nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))


def loginUser(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('privado')
				else:
					return render_to_response('competition/noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('competition/nousuario.html',context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('competition/ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/login')
def privado(request):
	usuario = request.user
	return render_to_response('competition/privado.html', {'usuario':usuario}, context_instance=RequestContext(request))


@login_required(login_url='/login')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

#Nomes registra equip
def nuevo_equipo(request):
	if request.method=='POST':
		formulario = nouEquip(request.POST, request.FILES)
		if formulario.is_valid():
			equip = formulario.save()
			request.equip = equip
			return render_to_response('competition/teamokey.html',{'equip':equip})
			
	else:
		formulario = nouEquip()
	return render_to_response('competition/equipform.html',{'formulario':formulario},context_instance=RequestContext(request))

#Registra equip i jugadors:
def nuevo_equipo_jugador(request):
	if request.method=='POST':
		form_team = nouEquip(request.POST, request.FILES)
		form_player = jugadorForm(request.POST, request.FILES)
		if form_team.is_valid():
			equip = form_team.save()
			form_player.team = equip
			if form_player.is_valid():
				form_player.save()
				return render_to_response('competition/teamokey.html',{'equip':equip})
	else:
		form_team = nouEquip()
		form_player = jugadorForm()
	return render_to_response('competition/equipform.html',{'form_team':form_team,'form_player':form_player},context_instance=RequestContext(request))




@login_required(login_url='/login')
def nuevo_jugador(request):
	equip = Equip.objects.get(username__iexact = unicode(request.user.username))
	if request.method=='POST':
		formulario = jugadorForm(equip,request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = jugadorForm(equip)
	return render_to_response('competition/jugadorform.html',{'formulario':formulario}, context_instance=RequestContext(request))

class recountInsc(ListView):
	#totsEquips = Equip.objects.all()
	#queryset = totsEquips.count()
	context_object_name='total'
	template_name='competition/recount.html'
	def __init__(self):
		self.totsEquips = Equip.objects.all()
		self.queryset = self.totsEquips.count()
	

class jugadorsInscrits(ListView):
	pass
	"""
	equip = Equip
	queryset = Jugador.objects.filter(team = equip)
	context_instance = 'listJugadors'
	template_name='competition/jugadorsList.html'

	def __init__(self,request,*args):
		super(jugadorsInscrits,self).__init__(*args)
		self.equip = Equip.objects.get(username__iexact=unicode(request.user.username))

		
		queryset = Equip.objects.filter(team = equipAux)
		context_instance = 'listJugadors'
		template_name='competition/jugadorsList.html'

"""