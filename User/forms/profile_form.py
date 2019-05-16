from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from User.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user"]

        widgets = {
            "profile_image": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em', 'placeholder':'Input the url for your image'}),
            "phone": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "street": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "zip_code": widgets.Select(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "ssn": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'})
        }


class AuthUser(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined',
                   'user_permissions', 'groups']
        widgets = {
            "username": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "first_name": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "last_name": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "email": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
        }
        help_texts = {
            "username": ""
        }
