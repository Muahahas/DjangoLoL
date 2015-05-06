from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import ListView
from models import *

# Create your views here.

class indexView(ListView):
	template_name = 'competition/index.html'
	queryset=Equip.objects.all()
