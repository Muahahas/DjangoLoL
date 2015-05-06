from django.forms import ModelForm
from django import forms
from competition.models import Equip
from django.utils.translation import ugettext, ugettext_lazy as _


class EquipForm(ModelForm):
	class Meta:
		model = Equip
		exclude = ['groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined']


class nouEquip(ModelForm):

	error_messages = {
		'duplicate_username': _("A user with that username already exists."),
		'password_mismatch': _("The thwo passord fields didn't match."),
	}
	username = forms.RegexField(label=_("Username"),max_length=30,
			regex=r'^[\w.@+-]+$',
			help_text=_("Required. 30 characters or fewer. Letters, digits and ""@/./+/-/_ only."),
			error_messages = {'invalid':_("This value may contain only letters, numbers and ""@/./+/-/_ characters.")})
	password1 = forms.CharField(label=_("Password"),
		widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"),
		widget=forms.PasswordInput,
		help_text=_("Enter the same passord as above, for verification"))

	class Meta:
		fields = ("username","email",)
		model = Equip
		exclude = ['groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined']

	def save(self, commit=True):
		equip = super(nouEquip, self).save(commit=False)
		equip.set_password(self.cleaned_data["password1"])
		if commit:
			equip.save()
		return equip