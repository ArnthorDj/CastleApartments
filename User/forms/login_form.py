from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'max-width: 35em'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Password', 'style': 'max-width: 35em'}))

    class Meta:
        model: User
        fields = ['username', 'password']
