from django import forms

class ContactoForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        label='Asunto',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    body = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )