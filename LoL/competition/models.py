# -*- coding: utf-8 -*-
from django.db import models
import datetime
from datetime import datetime
#from django.utils import timezone
from django.contrib import auth
# Create your models here.

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

class EquipXML(models.Model):
	username = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	isTeamValid = models.BooleanField(default=False)

	def __init__(self, equip):
		self.username = equip.username
		self.email = equip.correoe
		self.isTeamValid = equip.isTeamValid
		#self.players = list(Jugador.objects.filter(team=equip))


class Jugador(models.Model):
	ROL_CHOICES = [
		('Top','Top'),
		('ADC', 'AD Carry'),
		('Sup','Support'),
		('Jun','Jungle'),
		('Mid','Middle'),
	]

	name = models.CharField(max_length=50)
	rol =  models.CharField(max_length=3, choices=ROL_CHOICES)
	top = models.BooleanField(default=False)
	team = models.ForeignKey(Equip)
	email = models.EmailField()#unique=True)

	def __unicode__(self):
		return u"%s" % self.name


class Lliga(models.Model):
	codi = models.IntegerField(default=0)
	equips = models.ManyToManyField(Equip)

	def __unicode__(self):
		return u'Lliga nº %d' % (self.codi)

class Jornada(models.Model):
	codi = models.IntegerField(default=0)
	date = models.DateTimeField(default=datetime.now())
	league = models.ForeignKey(Lliga)
	iniciada = models.BooleanField(default=False)
	acabada = models.BooleanField(default=False)
	isReady = models.BooleanField(default=False)

	def __unicode__(self):
		return u'Jornada nº %d de la  %s' % (self.codi, self.league)

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
		return u'Partida nº %d de la %s' % (self.codi, self.jornada)

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
		return u'Classificacio de la lliga: nº %d' % self.league.codi 
	

class EquipPosition(models.Model):
	points = models.IntegerField(default=0)
	equip = models.ForeignKey(Equip)
	clas = models.ForeignKey(Classificacio)

	class Meta:
		ordering = ['points']

	def __unicode__(self):
		return u'%s          Points: %d' % (self.equip,self.points)





class Reclamacio(models.Model):
		team = models.ForeignKey(Equip)	
		jornada = models.ForeignKey(Jornada)
		lliga = models.ForeignKey(Lliga)
		jugador = models.ForeignKey(Jugador)
		partida = models.ForeignKey(Partida)

		text = models.CharField(max_length=300)

		class Meta:
			unique_together = ['jugador','partida']
