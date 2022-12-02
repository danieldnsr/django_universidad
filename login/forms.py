from django import forms


class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=255, label="", widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    contrasenia  = forms.CharField(max_length=255, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Contesenia'}))