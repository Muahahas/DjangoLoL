from django.shortcuts import render, render_to_response, RequestContext
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import ListView
from models import *

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
			return HttpResponse('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))