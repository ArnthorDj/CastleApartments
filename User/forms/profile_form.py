from django.forms import ModelForm, widgets, forms
from django.contrib.auth.models import User
from User.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user"]

        widgets = {
            "profile_image": widgets.TextInput(),
            "phone": widgets.TextInput()
        }


class AuthUser(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups']
        widgets = {
            "first_name": widgets.TextInput(),
            "last_name": widgets.TextInput(),
            "email": widgets.TextInput(),
        }
