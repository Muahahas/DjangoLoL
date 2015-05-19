from django.shortcuts import render, render_to_response, RequestContext
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from models import *
from forms import *
from django import forms as django_forms
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
import unicodedata
from datetime import datetime
from django.core.mail import EmailMessage
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers
import json
import smtplib
import string
import urllib2
import random

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
class ConnegResponseMixin(TemplateResponseMixin):

    def render_xml_object_response(self, objects, **kwargs):
    	if objects[0].__class__ == Lliga:
    		object_list = Jornada.objects.filter(league=objects[0])
    		objects = objects + list(object_list)
    	elif objects[0].__class__ == Equip:
    		object_list = Jugador.objects.filter(team=objects[0])
    		objects = objects + list(object_list)
    	xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            return self.render_xml_object_response(objects=objects)
        else:
            return super(ConnegResponseMixin, self).render_to_response(context)

class jugadorComprovacio():
		nom=""
		email=""

def Comprovacio(equip, players):
	json_file = 'jugadors.json'
	juga = jugadorComprovacio()		
	#jugadors= '0'
   	json_data=open(json_file)
   	data = json.load(json_data)
   	json_data.close()
   	listjugadors=list()
   	for i in range(len(data["jugadors"])):
   		juga.nom=data["jugadors"][i]["nom"]
   		juga.email=data["jugadors"][i]["correu"]
   		listjugadors.append(juga)
   		juga = jugadorComprovacio()
	a = True
	for item in players:
		b = False
		for player in listjugadors:
			print player.nom, player.email
			print item.name, item.email
			if item.name == player.nom and item.email == player.email:
				b = True
		print b	
		a = a and b
		print a

	if a:
		equip.validat()
	else:
		equip.desvalidar()



class indexView(ListView):
	template_name = 'competition/index.html'
	queryset=Equip.objects.all()

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

def isRolAndNameValid(list,n):
	a = True
	if n == len(list):
		return a
	for item in list[n+1:]:
		a = a and item.name != list[n].name and item.rol != list[n].rol
	return a and isRolAndNameValid(list,n+1)


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



def enviarConfirmacio(equip, players):
	username = "ebm7@alumnes.udl.cat"
	password = "1994iole"
	body_text = "El equip %s ha sigut registrat amb els jugadors %s, %s, %s, %s i %s" % (equip, players[0],players[1],players[2],players[3],players[4])
	toaddrs = []
	toaddrs.append(equip.correoe)
	for item in players:
		toaddrs.append(item.email)
	server = smtplib.SMTP('alumnes.udl.cat:465')
	BODY = string.join((
            "From: %s" % username,
            "To: %s" % ', '.join(toaddrs),
            "Subject: Equip registrat a la competicio de lol" ,
            "",
            body_text
            ), "\r\n")
	server.starttls()
	server.login(username,password)
	try:
		server.sendmail(username, toaddrs, BODY)
		server.quit()
	except:
		server.quit()
		return HttpResponse('Error')
	return HttpResponse('Enviat')



#Registra equip i jugadors:


def nuevo_equipo_jugador(request):
	if request.method=='POST':
		names = request.POST.getlist('name')
		roles = request.POST.getlist('rol')
		emails = request.POST.getlist('email')
		
		requestForm = [request.POST.copy() for count in xrange(5)]
		for item in requestForm:
			item.__setitem__('name',names.pop(0))
			item.__setitem__('rol',roles.pop(0))
			item.__setitem__('email',emails.pop(0))
		
		form_team = nouEquip(request.POST, request.FILES,)
		form_player_list = [jugadorForm(requestForm.pop(0),request.FILES,) for count in xrange(5)]

		
		if form_team.is_valid():
			equip = form_team.save(commit=False)
			for item in form_player_list:
				item.team = equip
			if isTeamValid(form_player_list):# and form2.is_valid():
				equip = form_team.save()
				players = teamSave(form_player_list)
				Comprovacio(equip,players)
				enviarConfirmacio(equip,players)
				return render_to_response('competition/teamokey.html',{'equip':equip,'players':players})
	else:
		form_team = nouEquip()
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

	context_object_name='total'
	template_name='competition/recount.html'
	def __init__(self):
		self.queryset = Equip.objects.all()



@login_required(login_url='/login')
def inscrits(request):
	if request.user.is_staff:
		llista = []
	else:
		equip = Equip.objects.get(username__iexact=unicode(request.user.username))
		llista = Jugador.objects.filter(team = equip)
	return render_to_response('competition/jugadorsList.html',{'llista':llista}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def editPlayers(request):
	equip = Equip.objects.get(username__iexact=unicode(request.user.username))
	llista = list(Jugador.objects.filter(team=equip))
	
	if request.method=='POST':		
		names = request.POST.getlist('name')
		roles = request.POST.getlist('rol')
		emails = request.POST.getlist('email')
		requestForm = [request.POST.copy() for count in xrange(5)]
		for item in requestForm:
			item.__setitem__('name',names.pop(0))
			item.__setitem__('rol',roles.pop(0))
			item.__setitem__('email',emails.pop(0))
		form_player_list = [jugadorForm(requestForm.pop(0),request.FILES, instance=llista.pop(0)) for count in xrange(5)]
		for item in form_player_list:
				item.team = equip
		if isTeamValid(form_player_list):
			players = teamSave(form_player_list)
			Comprovacio(equip,players)
			return HttpResponseRedirect('/jugadors')
	else:
		form_player_list = [jugadorForm(instance=llista.pop(0)) for count in xrange(5)]
	return render_to_response('competition/equipedit.html',{'form_player_list':form_player_list}, context_instance=RequestContext(request))






class  teamDetail(DetailView, ConnegResponseMixin):
	model = Equip
	template_name = 'competition/team_detail.html'


	def get_context_data(self, **kwargs):
		context = super(teamDetail,self).get_context_data(**kwargs)
		return context


def validate(request, pk):	
	team = Equip.objects.get(id=pk)
	if team.isTeamValid:
		team.desvalidar()
	else:
		team.validat()	
	return HttpResponseRedirect('/team/%s/' % (pk))

def enviarInfo(request):
	pass
	

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
	if len(teams) % 2 == 1:
		teams.append(Equip())

	rounds = len(teams) - 1
	
	for i in xrange(rounds):
		if i % 2 == 0:
			jornadaParell(teams)
		else:
			jornadaImparell(teams)
		journey = Jornada()
		journey.date = datetime(2015,6,10,i,0,0)
		journey.codi = i+1
		journey.league = lliga
		journey.save()
		e = 0
		for team1, team2 in pairwise(teams):			
			match = Partida()
			match.jornada = journey
			match.save()
			if  team1.username == '':
				match.codi = 0
				match.equips.add(team2)
				match.acabada=True
			elif team2.username == '':
				match.codi = 0
				match.equips.add(team1)
				match.acabada=True
			else:
				match.codi = e+1
				print team1
				match.equips.add(team1)
				match.equips.add(team2)
				e+=1
			match.save()
				
		
		


def generarHoraris(request):
	lliguesAnteriors = list(Lliga.objects.all())
	if lliguesAnteriors:
		for item in lliguesAnteriors:
			item.delete()

	teams = list(Equip.objects.filter(isTeamValid = True))
	if not teams:
		return render_to_response('competition/pocsusers.html',{'n':0})
	elif len(teams) == 1:
		return render_to_response('competition/pocsusers.html',{'n':1})
	elif len(teams) == 2:
		return render_to_response('competition/pocsusers.html',{'n':2})

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
		lliga.codi = i+1
		lliga.save()
		for team in item:
			lliga.equips.add(team)
		lliga.save()
		generarJornades(item, lliga)
		i+=1
	
	return render_to_response('competition/calendariFet.html',{'n':i},context_instance=RequestContext(request))

class viewCalendar(ListView):
	queryset = Lliga.objects.all()
	context_object_name = 'list'
	template_name = 'competition/calendari.html'

	def	get_context_data(self, **kwargs):
		context	= super(viewCalendar, self).get_context_data(**kwargs)	
		return context

class leagueDetail(DetailView, ConnegResponseMixin):
	model = Lliga
	template_name = 'competition/league_detail.html'

	def get_context_data(self, **kwargs):
		context = super(leagueDetail,self).get_context_data(**kwargs)
		return context

def getStatus(request):
	#lol = LeagueOfLegends('e34cddf8-4d00-41e9-9ff7-e744f7fb189c')
	regions = ['br','eune','euw','lan','las','oce','ru','tr'] #'pbe'
	stats = ['online','alert','offline','deploying']
	url = ["http://status.leagueoflegends.com/shards/%s" % (item) for item in regions]
	try:
		response =[urllib2.urlopen(add) for add in url]
	except urllib2.HTTPError, err:
		return render_to_response('competition/servers.html',{'err':err},context_instance=RequestContext(request))
	except urllib2.URLError, err:
		return render_to_response('competition/servers.html',{'err':err},context_instance=RequestContext(request))

   	data = [json.load(resp) for resp in response]
   	status = dict(zip([item["name"] for item in data],[item["services"][1]["status"] for item in data]))
   	status["Brazil"]=stats[1]
   	status["Turkey"]=stats[2]
   	status["Oceania"]=stats[3]
   	return render_to_response('competition/servers.html',{'status':status,'stats':stats},context_instance=RequestContext(request))

@login_required(login_url='/login')
def sendReclamation(request):
	equip = Equip.objects.get(username__iexact = unicode(request.user.username))

	if request.method=='POST':
		formulario = reclamacioForm(equip, request.POST, request.FILES)
		formulario.team = equip
		formulario.jugador = Jugador.objects.get(id=request.POST.__getitem__('jugador'))
		formulario.partida = Partida.objects.get(id=request.POST.__getitem__('partida'))
		formulario.jornada = formulario.partida.jornada
		formulario.lliga = formulario.jornada.league
		if formulario.is_valid():
			reclamacio = formulario.save()
			return HttpResponse("Guardat")
	else:
		formulario = reclamacioForm(equip)

	return render_to_response('competition/reclamacioform.html',{'formulario':formulario},context_instance=RequestContext(request))

class jornadesList(ListView):
	queryset = Jornada.objects.filter(iniciada=False, acabada=False).order_by('date')[:5]
	context_object_name = 'listJornades'
	template_name = 'competition/jornades_list.html'


class jornadaDetail(DetailView):
	model = Jornada
	template_name = 'competition/jornada_detail.html'


	def get_context_data(self, **kwargs):
		context = super(jornadaDetail,self).get_context_data(**kwargs)
		return context

class jornadesComensades(ListView):
	queryset = Jornada.objects.filter(iniciada=True, acabada=False).order_by('date')
	context_object_name = 'listJornades'
	template_name = 'competition/jornades_listC.html'

def getTeamsWaiting():
	pass

def asignIP():
	pass

def createResults(journey):
	partides = Partida.objects.filter(jornada=journey)
	for partida in partides:
		result = Resultat()
		result.partida = partida
		if partida.codi > 0:
			result.winner = random.randint(0,2)
			print result.winner
		result.save()	

def startJourney(request,pk):
	journey = Jornada.objects.get(id=pk)
	getTeamsWaiting()
	asignIP()
	createResults(journey)
	journey = Jornada.objects.get(id=pk)
	partides = Partida.objects.filter(jornada=journey)
	if not journey.iniciada and not journey.acabada:
		journey.start()
	for item in partides:
		item.start()
	return HttpResponseRedirect('/jornades/%s/' % (pk))

def getResults(journey):
	partides = Partida.objects.filter(jornada=journey)
	results = []
	for partida in partides:
		results = results + list(Resultat.objects.filter(partida=partida))
	return results




def createClasification(journey):
	classificacions_anteriors = Classificacio.objects.filter(league=journey.league)
	if classificacions_anteriors:
		for clas in classificacions_anteriors:
			EquipPosition.objects.filter(clas=clas).delete()
		classificacions_anteriors.delete()
	clasification = Classificacio()
	lliga = Lliga.objects.get(id=journey.league.id)
	clasification.league = journey.league
	clasification.save()
	for item in journey.league.equips.all():
		aux = EquipPosition()
		aux.points=0
		aux.equip = item
		aux.clas = clasification
		aux.save()		
	

	
def updateClasification(results, journey):
	clasification = Classificacio.objects.get(league=journey.league)	
	for item in results:
		partida = item.partida
		if item.winner == 1 and partida.codi > 0:
			aux = list(EquipPosition.objects.filter(clas=clasification, equip=partida.equips.all())).pop(0)
			print aux
			aux.points+=3
			aux.save()
		elif item.winner == 2 and partida.codi > 0:
			aux = list(EquipPosition.objects.filter(clas=clasification, equip=partida.equips.all())).pop(1)
			aux.points+=3
			aux.save()
	#print clasification.equips
	clasification.save()
		



def sendInfo(journey):
	clasification = Classificacio.objects.get(league=journey.league)
	partides = list(Partida.objects.filter(jornada=journey))
	results = [Resultat.objects.get(partida=partida) for partida in partides]
	username = "ebm7@alumnes.udl.cat"
	password = "1994iole"
	body_text = serializers.serialize(u"xml", [clasification]+partides+results)
	toaddrs = []
	toaddrs.append("marketing@mark.com")
	toaddrs.append("riot@lol.com")
	server = smtplib.SMTP('alumnes.udl.cat:465')
	BODY = string.join((
            "From: %s" % username,
            "To: %s" % ', '.join(toaddrs),
            "Subject: Final Jornada %s" % journey.codi ,
            "",
            body_text
            ), "\r\n")

	server.starttls()
	server.login(username,password)
	try:
		server.sendmail(username, toaddrs, BODY)
		server.quit()
	except:
		server.quit()
		return HttpResponse('Error')
	return HttpResponse('Enviat')

def finishMatch(request,pk):
	match = Partida.objects.get(id=pk)
	match.finish()
	match.save()
	return HttpResponseRedirect('/jornades/%s/' % (match.jornada.id))


def finishJourney(request, pk):
	journey = Jornada.objects.get(id=pk)
	results = getResults(journey)
	if journey.codi == 1:
		createClasification(journey)
	updateClasification(results,journey)
	sendInfo(journey)	
	if journey.iniciada and not journey.acabada:
		journey.finish()
	return HttpResponseRedirect('/jornades/%s/' % (pk))


def viewClasification(request):
	clasification = Classificacio.objects.all()
	positions = [list(EquipPosition.objects.filter(clas=clasif).order_by('points')) for clasif in clasification]
	for item in positions:
		item.reverse()
	return render_to_response('competition/clasification.html',{'clasification':clasification,'positions':positions, 'rounds':xrange(clasification.count())},context_instance=RequestContext(request))
