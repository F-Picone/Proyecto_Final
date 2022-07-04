from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ['username', 'email', 'passowrd1', 'password2']
        help_text = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Modificar contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Modificar apellido")
    first_name = forms.CharField(label="Modificar nombre")

    class meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'passowrd1', 'password2']
        help_text = {k:"" for k in fields}
        


