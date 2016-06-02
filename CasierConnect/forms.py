# -*- coding: utf-8 -*-
from django import forms
from .models import Casier
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Div

class CasierForm(forms.ModelForm):
	class Meta:
		model = Casier
		exclude = ('user', 'libre', 'date')

	def __init__(self, *args, **kwargs):
		super(CasierForm, self).__init__(*args, **kwargs)

		# If you pass FormHelper constructor a form instance
		# It builds a default layout with all its fields
		self.helper = FormHelper(self)
		self.helper.layout=Layout(
			# HTML(u"""<h2 class="section-title">Demande de Casier</h2>"""),	
			Fieldset(
				"Les champs marqués d'une * sont obligatoires",
				'email',
				'pseudo',
				'objet',
				),
			ButtonHolder(
				Submit('submit', 'Enregistrer',css_class = 'btn btn-warning btn-block btn-lg'), 
				)
			)
		# You can dynamically adjust your layout

class ConnexionForm(forms.Form):
	username = forms.CharField(label=u"Nom d'utilisateur", max_length=250)
	password = forms.CharField(label=u"Mot de passe", widget=forms.PasswordInput)
	
	def __init__(self, *args, **kwargs):
		super(ConnexionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.layout=Layout(
			Fieldset("Identifiez vous",'username','password'),
			ButtonHolder(
				Submit('submit', 'Connexion',css_class='btn btn-primary btn-block btn-lg'), 
				),
			)