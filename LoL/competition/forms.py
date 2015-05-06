from django.forms import ModelForm
from django import forms
from competition.models import Equip


class EquipForm(ModelForm):
	class Meta:
		model = Equip
		exclude = ['groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined']