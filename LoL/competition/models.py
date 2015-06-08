# -*- coding: utf-8 -*-
from django.db import models
import datetime
from datetime import datetime
#from django.utils import timezone
from django.contrib import auth
# Create your models here.
import dexml
from dexml import fields
class Equip(auth.models.User):
	
	correoe = models.EmailField('email',null=False,unique=True,)
	isTeamValid = models.BooleanField(default=False)
	isReady = models.BooleanField(default=False)

	def __unicode__(self):
		return u'Team ' + super(self.__class__, self).get_username()
	
	def validat(self):
		self.isTeamValid = True
		self.save()
		
	def desvalidar(self):
		self.isTeamValid = False
		self.save()

	def ready(self):
		self.isReady = True
		self.save()

	def unready(self):
		self.isReady=False
		self.save()

class Jugador(models.Model):
	ROL_CHOICES = [
		('Top','Top'),
		('ADC', 'AD Carry'),
		('Sup','Support'),
		('Jun','Jungle'),
		('Mid','Middle'),
	]

	name = models.CharField(max_length=50)
	rol =  models.CharField(max_length=3, blank=False,choices=ROL_CHOICES)
	top = models.BooleanField(default=False)
	team = models.ForeignKey(Equip)
	email = models.EmailField()#unique=True)
	
	def isTop(self):
		self.top = True
		self.save()

	def __unicode__(self):
		return u"%s" % self.name

class JugadorXML(dexml.Model):
	name = fields.String()
	rol = fields.String()
	email = fields.String()

	def __init__(self, player):
		self.name = player.name
		self.rol = player.rol
		self.email = player.email


class EquipXML(dexml.Model):
	username = fields.String()
	email = fields.String()
	players = fields.List(Jugador)
	

	def __init__(self, equip):
		self.username = equip.username
		self.email = equip.correoe
		for item in Jugador.objects.filter(team=equip):
			self.players.append(JugadorXML(item))





class Lliga(models.Model):
	codi = models.IntegerField(default=0)
	equips = models.ManyToManyField(Equip)
	finished = models.BooleanField(default=False)

	def finish(self):		
		self.finished = True
		self.save()

	def __unicode__(self):
		return u'Lliga n %d' % (self.codi)

class Jornada(models.Model):
	codi = models.IntegerField(default=0)
	date = models.DateTimeField(default=datetime.now())
	league = models.ForeignKey(Lliga)
	iniciada = models.BooleanField(default=False)
	acabada = models.BooleanField(default=False)
	isReady = models.BooleanField(default=False)

	def __unicode__(self):
		return u'Jornada n %d de la  %s' % (self.codi, self.league)

	def start(self):
		self.iniciada = True
		self.save()

	def finish(self):
		self.iniciada = False
		self.acabada = True
		self.save()

	def ready(self):
		self.isReady=True
		self.save()

	def partidesAcabades(self):
		partida = Partida.objects.filter(jornada=self)
		a = True
		for item in partida:
			a = a and item.acabada
		return a


class Partida(models.Model):
	codi = models.IntegerField(default=0)
	ip = models.CharField(max_length= 15)
	equips = models.ManyToManyField(Equip)
	jornada = models.ForeignKey(Jornada)
	iniciada = models.BooleanField(default=False)
	acabada = models.BooleanField(default=False)

	def setIP(self,ip):
		self.ip = ip
		self.save()

	def finish(self):
		self.acabada = True
		self.iniciada = False
		self.save()

		
	def start(self):
		self.iniciada = True
		self.save()

	def __unicode__(self):
		return u'Partida n %d de la %s' % (self.codi, self.jornada)

class PartidaXML(dexml.Model):
	codi = fields.Integer()
	ip = fields.String()
	equips = fields.List(Equip)
	def __init__(self, match):
		self.codi = match.codi
		self.ip = match.ip
		for item in match.equips.all():
			self.equips.append(EquipXML(item))




class JornadaXML(dexml.Model):
	codi = fields.Integer()
	date = fields.String()
	partides = fields.List(Partida)
	

	def __init__(self, jornada):
		self.codi = jornada.codi
		self.date = jornada.date
		for item in Partida.objects.filter(jornada=jornada):
			self.partides.append(PartidaXML(item))


class LligaXML(dexml.Model):
	codi = fields.String()
	jornades = fields.List(Jornada)	

	def __init__(self, lliga):
		self.codi = lliga.codi
		for item in Jornada.objects.filter(league=lliga):
			self.jornades.append(JornadaXML(item))




class Estadistiques(models.Model):
	mortsEquip = models.IntegerField(default=0)
	killsEquip = models.IntegerField(default=0)
	assistEquip = models.IntegerField(default=0)
	
	team = models.ForeignKey(Equip)

	

class Resultat(models.Model):

	mortsEquipA = models.IntegerField(default=0)
	killsEquipA = models.IntegerField(default=0)
	assistEquipA = models.IntegerField(default=0)

	mortsEquipB = models.IntegerField(default=0)
	killsEquipB = models.IntegerField(default=0)
	assistEquipB = models.IntegerField(default=0)

	#0 = empat, 1 = winnerTeamA , 2 = winnerTeamB
	winner = models.IntegerField(default=0)

	partida = models.OneToOneField(Partida)

	def __unicode__(self):
		return u'Resultat de la %s' % self.partida


class Classificacio(models.Model):
	league = models.OneToOneField(Lliga)

	def __unicode__(self):
		return u'Classificacio de la lliga: n %d' % self.league.codi
	

class EquipPosition(models.Model):
	points = models.IntegerField(default=0)
	equip = models.ForeignKey(Equip)
	clas = models.ForeignKey(Classificacio)

	class Meta:
		ordering = ['points']

	def __unicode__(self):
		return u'%s          Points: %d' % (self.equip,self.points)

class EquipPositionXML(dexml.Model):
	points = fields.Integer()
	equip = fields.String()

	def __init__(self,position):
		self.points = position.points
		self.equip = position.equip.username


class ClassificacioXML(dexml.Model):
	lliga = fields.String()
	positions = fields.List(EquipPosition)

	def __init__ (self, classificacio):
		self.lliga =u'Lliga num %d.' % classificacio.league.codi
		for item in EquipPosition.objects.filter(clas=classificacio):
			self.positions.append(EquipPositionXML(item))

class ResultXML(dexml.Model):
	mortsEquipA = fields.Integer()
	killsEquipA = fields.Integer()
	assistEquipA = fields.Integer()

	mortsEquipB = fields.Integer()
	killsEquipB = fields.Integer()
	assistEquipB = fields.Integer()

	winner = fields.Integer()

	partida = fields.String()

	def __init__ (self, result):
		self.mortsEquipA = result.mortsEquipA
		self.killsEquipA = result.killsEquipA
		self.assistEquipA = result.assistEquipA
		self.mortsEquipB = result.mortsEquipB
		self.killsEquipB = result.killsEquipB
		self.assistEquipB = result.assistEquipB

		self.winner = result.winner

		self.partida = u'Partida num %d' % result.partida.codi



class Reclamacio(models.Model):
	team = models.ForeignKey(Equip)	
	jornada = models.ForeignKey(Jornada)
	lliga = models.ForeignKey(Lliga)
	jugador = models.ForeignKey(Jugador)
	partida = models.ForeignKey(Partida)
	text = models.CharField(max_length=300)
	response = models.CharField(blank=True,max_length=300)
	solved = models.BooleanField(default=False)

	class Meta:
		unique_together = ['jugador','partida']

	def __unicode__(self):
		return u'Reclamacio de %s de la %s' % (self.jugador, self.partida)

class Noticia(models.Model):
	titol = models.CharField(max_length=50)
	cosNoticia = models.CharField(max_length=400)
	date = models.DateTimeField(default=datetime.now())

	def __unicode__(self):
		return u'%s' % self.titol
