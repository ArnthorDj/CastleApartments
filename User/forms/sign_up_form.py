from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets, ModelForm
from django import forms
from django.contrib.auth.models import User
from User.models import Profile
from RealEstate.models import RealEstates


class AuthUserForm(ModelForm):
     model = User
     exclude = ['id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined',
                'user_permissions', 'groups']
     widgets = {
        "username": widgets.TextInput(),
        "first_name": widgets.TextInput(),
        "last_name": widgets.TextInput(),
        "email": widgets.TextInput(),
        "password": widgets.HiddenInput(),
        "confirm password": widgets.HiddenInput()
    }

class UserProfile(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user",'profile_image']
        widgets = {
            "SSN": widgets.NumberInput(),
            "phone": widgets.TextInput()

        }

class ContactInformationForm(ModelForm):
    class Meta:
        model = RealEstates
        exclude = ['size','bedrooms','bathrooms','type','price','more_info','main_image','on_sale','seller']
        widgets = {
            "country": widgets.Select(),
            "street": widgets.TextInput(),
            "city": widgets.TextInput(),
            "zip": widgets.NumberInput()
            #"on_sale": widgets.HiddenInput()
            }

