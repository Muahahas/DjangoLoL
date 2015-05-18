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
		

	def __unicode__(self):
		return u'Team ' + super(self.__class__, self).get_username()
	
	def validat(self):
		self.isTeamValid = True
		self.save()
		
	def desvalidar(self):
		self.isTeamValid = False
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

	def __unicode__(self):
		return u'Jornada nº %d de la  %s' % (self.codi, self.league)

	def start(self):
		self.iniciada = True
		self.save()

	def finish(self):
		self.iniciada = False
		self.acabada = True
		self.save()

class Partida(models.Model):
	codi = models.IntegerField(default=0)
	ip = models.CharField(max_length= 15)
	equips = models.ManyToManyField(Equip)
	jornada = models.ForeignKey(Jornada)
	iniciada = models.BooleanField(default=False)
	acabada = models.BooleanField(default=False)

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

class Classificacio(models.Model):
	league = models.OneToOneField(Lliga)
	equips = dict()





class Reclamacio(models.Model):
		team = models.ForeignKey(Equip)	
		jornada = models.ForeignKey(Jornada)
		lliga = models.ForeignKey(Lliga)
		jugador = models.ForeignKey(Jugador)
		partida = models.ForeignKey(Partida)

		text = models.CharField(max_length=300)

		class Meta:
			unique_together = ['jugador','partida']
