from django.shortcuts import render, render_to_response, RequestContext
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
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

def nuevo_equipo(request):
	if request.method=='POST':
		formulario = EquipForm(request.POST, request.FILES)
		if formulario.is_valid():
			equip = formulario.save()
			return render_to_response('competition/teamokey.html',{'equip':equip})
			
	else:
		formulario = EquipForm()
	return render_to_response('competition/equipform.html',{'formulario':formulario},context_instance=RequestContext(request))

