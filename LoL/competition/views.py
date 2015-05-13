from django.shortcuts import render, render_to_response, RequestContext
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from models import *
from forms import *
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
import unicodedata
from django.core.mail import EmailMessage

from itertools import izip
import math
import decimal
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
	if usuario.is_staff:	
		return render_to_response('competition/privado.html', {'usuario':usuario}, context_instance=RequestContext(request))	
	else:
		equip = Equip.objects.get(username__iexact = unicode(usuario.username))
		return render_to_response('competition/privado.html', {'usuario':usuario,'equip':equip}, context_instance=RequestContext(request))



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
		form_player_list = [jugadorForm(requestForm.pop(0),request.FILES,) for count in xrange(5)]

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
				#return HttpResponseRedirect()
				enviarComprovacio(equip,players)
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
	context_object_name='total'
	template_name='competition/recount.html'
	def __init__(self):
		self.queryset = Equip.objects.all()
		#self.queryset = Equip.objects.filter(isTeamValid=True)
		#self.queryset = self.totsEquips.count()


@login_required(login_url='/login')
def inscrits(request):
	if request.user.is_staff:
		llista = []
	else:
		equip = Equip.objects.get(username__iexact=unicode(request.user.username))
		llista = Jugador.objects.filter(team = equip)	
	#template_name = 'competition/jugadorsList.html'
	return render_to_response('competition/jugadorsList.html',{'llista':llista}, context_instance=RequestContext(request))

class  teamDetail(DetailView):
	model = Equip
	template_name = 'competition/team_detail.html'


	def get_context_data(self, **kwargs):
		context = super(teamDetail,self).get_context_data(**kwargs)
		return context
		
def enviarComprovacio(equip, players):
	team = equip
	jugadors = Jugador.objects.filter(team=equip)
	subject = "Validate %s" % (equip)
	body = "Team: %s Players: 1- %s   2- %s   3- %s   4- %s   5- %s" % (equip, jugadors[0], jugadors[1], jugadors[2], jugadors[3], jugadors[4])
	from_email = "admin@admin.com"
	to = ["checkTop@riot.com"]
	mail = EmailMessage(subject,body,from_email,to)
	try:
		imail.send()
		print "sent"
		#return HttpResponseRedirect('/validate', {'equip':equip,'players':jugadors},context_instance=RequestContext(request))
	except:
		print "not send"
		#return HttpResponseRedirect('/validate', {'equip':equip,'players':jugadors},context_instance=RequestContext(request))





def enviarInfo(request):
	if request.method=='POST':
		formulario = email(request.POST,request.FILES)
		if formulario.is_valid():
			subject = request.POST.__getitem__('asunto')
			body = request.POST.__getitem__('mensaje')
			from_email = request.POST.__getitem__('remitente')
			to = [request.POST.__getitem__('destinatari')]
			attach = request.POST.__getitem__('attach')

			if attach :
				imail = EmailMessage(subject,body,from_email,to,attachments=attach)
				#return HttpResponse("Attach")
			else:
				imail = EmailMessage(subject,body,from_email,to)
				#return HttpResponse("No attach")
			try:
				imail.send()
				return HttpResponse('Enviat')
			except:
				return HttpResponse('Error')
	else:
		formulario = email()
	return render_to_response('competition/enviarinfo.html',{'formulario':formulario},context_instance=RequestContext(request))


def validate(request, pk):
	
	team = Equip.objects.get(id=pk)

	#team.isValidTeam = True
	if team.isTeamValid:
		team.desvalidar()
	else:
		team.validat()	
	return HttpResponseRedirect('/team/%s/' % (pk))


#def enviarInfo(request):
#	if request.method=='POST':
#		formulario = email(request.POST,request.FILES)
#		if formulario.is_valid():
#			mail = """From: %s
#			To: %s
#			MIME-Version: 1.0
#			Content-type: text/html
#			Subject: %s
#			%s
#			""" % (request.POST.__getitem__('remitente'), request.POST.__getitem__('destinatari'), request.POST.__getitem__('asunto'), request.POST.__getitem__('mensaje'))
#			try:
#				smtp = smtplib.SMTP('localhost')
#				smtp.sendmail(request.POST.__getitem__('remitente'), request.POST.__getitem__('destinatari'), email)
#				return HttpResponse('Enviat')
#			except:
#				return HttpResponse('ERROR AL ENVIAR EL MISSATGE')
#	else:
#		formulario = email()
#	return render_to_response('competition/enviarinfo.html',{'formulario':formulario},context_instance=RequestContext(request))
def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def jornadaParell(list):
	list.reverse()
	for e in xrange(len(list)/2 - 1):
		aux = list.pop(e)
		list.insert(e+3+e,aux)
	list.reverse()
	aux = list.pop(2)
	list.insert(-1,aux)
	print list

def jornadaImparell(list):
	aux = list.pop(-2)
	list.insert(1,aux)
	print list

def generarJornades(teams, lliga):
	if len(teams) % 2 == 0:
		print "parell"
		#return HttpResponse('Parell')
	else:
		print "imparell"
		teams.append(Equip())
		#return HttpResponse('Imparell')

	print teams
	rounds = len(teams) - 1
	
	for i in xrange(rounds):
		if i % 2 == 0:
			jornadaParell(teams)
			journey = Jornada()
			journey.codi = i
			journey.league = lliga
			journey.save()
				
		else:
			jornadaImparell(teams)
			journey = Jornada()
			journey.codi = i
			journey.league = lliga
			journey.save()
		e = 0
		for team1, team2 in pairwise(teams):			
			match = Partida()
			match.codi = e
			match.jornada = journey
			match.save()
			if  team1.username == '':
				match.equips.add(team2)	
			elif team2.username == '':
				match.equips.add(team1)
			else:
				match.equips.add(team1)
				match.equips.add(team2)	
			e+=1
		
		print teams


def generarHoraris(request):
	#pass
	teams = list(Equip.objects.filter(isTeamValid = True))
	if not teams:
		return HttpResponse('No hi ha cap equip validat')
	elif len(teams) == 1:
		return HttpResponse('Nomes hi ha un equip validat')
	elif len(teams) == 2:
		return HttpResponse('Nomes hi ha 2 equips validats')

	nLligues = math.ceil(float(len(teams))/float(24))
	if len(teams) % nLligues == 0:
		nPlayers = len(teams)/nLligues
		numLligues1JugadorMes = 0
	else:
		nPlayers = len(teams)/nLligues
		numLligues1JugadorMes = len(teams)%nLligues

	equipsPerLliga = []
	for i in xrange(int(nLligues-numLligues1JugadorMes)):
		equipsPerLliga.append([])
		for e in xrange(int(nPlayers)):
			equipsPerLliga[i].append(teams.pop(0))
	if numLligues1JugadorMes != 0:
		for i in xrange(numLligues1JugadorMes):
			for e in xrange(nPlayers+1):
				equipsPerLliga[i + nLligues].append(teams.pop(0))
	i = 0
	for item in equipsPerLliga:
		lliga = Lliga()
		lliga.codi = i
		lliga.save()
		generarJornades(item, lliga)
		i+=1

	
	return HttpResponse('FI')



