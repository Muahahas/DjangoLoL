from django.db import models
import datetime
from django.utils import timezone
from django.contrib import auth
# Create your models here.

class Equip(auth.models.User):
	def email():
		email = models.EmailField(null=False,unique=True)
		return email
	def __unicode__(self):
		return u'Team ' + super(self.__class__, self).get_username()

class Jugador(models.Model):
	ROL_CHOICES = (
		('Top','Top'),
		('ADC', 'AD Carry'),
		('Sup','Support'),
		('Jung','Jungle'),
		('Mid','Middle'),
	)

	name = models.CharField(max_length=50)
	rol =  models.CharField(max_length=3, choices=ROL_CHOICES)
	top = models.BooleanField(default=False)
	team = models.ForeignKey(Equip)

	def __unicode__(self):
		return u"%s" % self.name

class Lliga(models.Model):
	codi = models.IntegerField(default=0)

class Partida(models.Model):
	codi = models.IntegerField(default=0)
	ip = models.CharField(max_length= 15)


	equipA = models.ManyToManyField(Equip)
	#equipB = models.ForeignKey(Equip)


class Jornada(models.Model):
	date = models.DateTimeField(default=timezone.now())

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

	partida = models.OneToOneField(Partida)