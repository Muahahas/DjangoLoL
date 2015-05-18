from django.contrib import admin
from models import *

# Register your models here.

class EquipAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","email"]
	fieldsets = [(None,{'fields':['username','email','password','isTeamValid']})]

admin.site.register(Jugador)
admin.site.register(Equip,EquipAdmin)
admin.site.register(Lliga)
admin.site.register(Jornada)
admin.site.register(Partida)
admin.site.register(Resultat)
admin.site.register(Estadistiques)
admin.site.register(Reclamacio)
admin.site.register(Classificacio)
admin.site.register(EquipPosition)
