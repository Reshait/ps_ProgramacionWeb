from django import forms
from django.contrib.auth.models import User

class RegistroUsuario(forms.Form):
	nombreUsuario = forms.CharField(min_length=5)
	email = forms.EmailField()
	password = forms.CharField(min_length=5, widget=forms.PasswordInput())
	password2 = forms.CharField(min_length=5, widget=forms.PasswordInput())

	def usuarioUnico(self):
		nombreUsuario = self.cleaned_data['nombreUsuario']
		if User.objects.filter(nombreUsuario=nombreUsuario):
			raise forms.ValidationError('Nombre de usuario ya registrado.')
		return nombreUsuario

	def emailUnico(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('Ya existe un email igual.')
		return email

	def passOK(self):
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError('Los passwords no coinciden.')
		return password2

