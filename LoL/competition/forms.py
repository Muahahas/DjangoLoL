from django.forms import ModelForm, Form
from django import forms
from competition.models import Equip, Jugador
from django.utils.translation import ugettext, ugettext_lazy as _


"""class EquipForm(ModelForm):
	class Meta:
		model = Equip
		exclude = ['groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined']

"""


class jugadorForm(ModelForm):

	rol = forms.ChoiceField(label=_("Rol:"),required=False, choices=[('','-----')]+Jugador.ROL_CHOICES)

	class Meta:
		team = None
		model = Jugador
		exclude=['top','team',]
		fields = ("name","email","rol")

	def __init__(self, *args, **kwargs):
		#prefix = kwargs.pop('prefix',None)
		#if prefix != None:
		#	super(jugadorForm,self).__init__(*args,**kwargs)
		#else:
		super(jugadorForm,self).__init__(*args,**kwargs)
		self.team = None

	def save(self, commit=True):
		jugador = super(jugadorForm, self).save(commit=False)
		jugador.team = self.team
		if commit:
				jugador.save()
		return jugador


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
	correoe = forms.EmailField(label=_("Email"))

	class Meta:
		fields = ("username","correoe",)
		model = Equip
		exclude = ['groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined','isTeamValid']

	def save(self, commit=True):
		equip = super(nouEquip, self).save(commit=False)
		equip.set_password(self.cleaned_data["password1"])
		equip.email = equip.correoe
		if commit:
			equip.save()
		return equip


class email(Form):

	remitente = forms.EmailField(label=_("From:"),max_length=30)
	destinatari = forms.EmailField(label=_("To:"),max_length=30)
	asunto = forms.CharField(label=_("Subject:"),max_length=30)
	mensaje = forms.CharField(label=_("Messaje:"),max_length=300,widget=forms.Textarea)
	attach = forms.FileField(label=_("Attachment:"),required=False)
