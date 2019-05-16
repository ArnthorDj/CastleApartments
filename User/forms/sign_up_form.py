from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets, ModelForm
from django.contrib.auth.models import User
from User.models import Profile
from RealEstate.models import ZipCodes


class AuthUserForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ['id', 'last_login', 'password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups']
        widgets = {
            "username": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "first_name": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "last_name": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "email": widgets.EmailInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "password1": widgets.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "password2": widgets.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'})
        }
        help_texts = {
            "username": "",
        }



class UserProfile(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user", 'profile_image']

        widgets = {
            "ssn": widgets.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "phone": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "street": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
            "zip_code": widgets.Select(choices=[("1", "2")], attrs={'class': 'form-control', 'style': 'max-width: 20em'})
        }

# class ContactInformationForm(ModelForm):
#     class Meta:
#         model = ZipCodes
#         exclude = ['city', 'country']
#
#         choices = []
#         for zip_code in ZipCodes.objects.all().values('zip_code'):
#             choices.append((zip_code['zip_code'], zip_code['zip_code']))
#         widgets = {
#             "zip_code": widgets.Select(choices=choices)
#             #"country": widgets(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
#             #"street": widgets.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
#             #"city": widgets.Select(attrs={'class': 'form-control', 'style': 'max-width: 20em'}),
#             #"zip": widgets.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 20em'})
#             }
