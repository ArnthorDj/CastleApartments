from django.forms import ModelForm, widgets
from User.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user"]
        widgets = {
            "profile_image": widgets.TextInput(),
            "phone": widgets.TextInput()
        }
