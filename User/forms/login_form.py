from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Username', 'style':'max-width: 16em'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control','placeholder': 'Password','style':'max-width: 16em'}))



