from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets, ModelForm
# from django import forms
from django.contrib.auth.models import User
from User.models import Profile
from RealEstate.models import RealEstates


class AuthUserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups']
        widgets = {
            "username": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "first_name": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "last_name": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "email": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "password": widgets.HiddenInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "confirm password": widgets.HiddenInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'})
                    }


class UserProfile(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user",'profile_image']
        widgets = {
            "SSN": widgets.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "phone": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'})
        }


class ContactInformationForm(ModelForm):
    class Meta:
        model = RealEstates
        exclude = ['size', 'bedrooms', 'bathrooms', 'type', 'price', 'more_info', 'main_image', 'on_sale', 'seller']
        widgets = {
            "country": widgets.Select(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "street": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "city": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "zip": widgets.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'})
            # "on_sale": widgets.HiddenInput()
            }
