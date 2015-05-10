from django.shortcuts import render, render_to_response, RequestContext
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from models import *
from forms import *
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
import unicodedata



#imports login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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

#Nomes registra equip, no s'utilitza ja
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


def isTeamValid(list):
	a = True
	for item in list:
		a = a and item.is_valid()
	return a

def teamSave(list):
	 listP = []
	 for item in list:
	 	player = item.save()
	 	listP.append(player)
	 return listP

def isRolAndNameValid(list,n):
	a = True
	if n == len(list):
		return a
	for item in list[n+1:]:
		a = a and item.name != list[n].name and item.rol != list[n].rol
	return a and isRolAndNameValid(list,n+1)






#Registra equip i jugadors:


def nuevo_equipo_jugador(request):
	if request.method=='POST':
		names = request.POST.getlist('name')
		roles = request.POST.getlist('rol')
		
		requestForm = [request.POST.copy() for count in xrange(5)]
		for item in requestForm:
			item.__setitem__('name',names.pop(0))
			item.__setitem__('rol',roles.pop(0))
		#requestForm2 = request.POST.copy()
		#requestForm2.__setitem__('name',names.pop(0))
		form_team = nouEquip(request.POST, request.FILES,)
		form_player_list = [jugadorForm(requestForm.pop(),request.FILES,) for count in xrange(5)]

		#form1 = jugadorForm(requestForm.pop(), request.FILES, prefix='form-1')
		#form2 = jugadorForm(requestForm.pop(), request.FILES ,prefix='form-2')
		if form_team.is_valid():
			equip = form_team.save(commit=False)
			#form1.team = equip	
			#form2.team = equip		
			for item in form_player_list:
				item.team = equip
			if isTeamValid(form_player_list):# and form2.is_valid():
				equip = form_team.save()
				#form1.save()
				#form2.save()			
				players = teamSave(form_player_list)
				return render_to_response('competition/teamokey.html',{'equip':equip,'players':players})
	else:
		form_team = nouEquip()
		#form1 = jugadorForm(prefix='form-1')
		#form2 = jugadorForm(prefix='form-2')
		form_player_list = [jugadorForm() for count in xrange(5)]

	return render_to_response('competition/equipform.html',{'form_team':form_team, 'form_player_list':form_player_list},context_instance=RequestContext(request))






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
"""	
@login_required(login_url='/login')
class jugadorsInscrits(ListView):
	queryset = Jugador.objects.filter(team = None)
	equip = Equip
	context_object_name = 'listJugadors'
	template_name='competition/jugadorsList.html'

	def __init__(self, request, *args, **kwargs):
		request = kwargs.pop('request',None)
		#nom = request.user.username
		self.equip = Equip.objects.get(username__iexact=unicode(self.request.user.username))		
		queryset = Jugador.objects.filter(team = self.equip)
		context_object_name = 'listJugadors'
		template_name='competition/jugadorsList.html'

"""
@login_required(login_url='/login')
def inscrits(request):
	equip = Equip.objects.get(username__iexact=unicode(request.user.username))
	llista = Jugador.objects.filter(team = equip)	
	#template_name = 'competition/jugadorsList.html'
	return render_to_response('competition/jugadorsList.html',{'llista':llista}, context_instance=RequestContext(request))