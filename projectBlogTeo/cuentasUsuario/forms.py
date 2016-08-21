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


class EditarEmailForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        """Obtener request"""
        self.request = kwargs.pop('request')
        return super(EditarEmailForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        # Comprobar si ha cambiado el email
        actual_email = self.request.user.email
        username = self.request.user.username
        if email != actual_email:
            # Si lo ha cambiado, comprobar que no exista en la db.
            # Exluye el usuario actual.
            existe = User.objects.filter(email=email).exclude(username=username)
            if existe:
                raise forms.ValidationError('Ya existe un email igual en la db.')
        return email

class EditarContrasenaForm(forms.Form):

    actual_password = forms.CharField(
        label='Password actual',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        label='Nueva password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(
        label='Repetir password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Los paswords no coinciden.')
        return password2