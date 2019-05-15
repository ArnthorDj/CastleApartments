from django.shortcuts import render, redirect
from User.models import Profile
from User.forms.profile_form import ProfileForm, AuthUser
from django.contrib.auth.models import User
from User.forms.sign_up_form import UserProfile, AuthUserForm#, ContactInformationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        auth_user_form = AuthUserForm(data=request.POST)
        user_profile_form = UserProfile(data=request.POST)

        if auth_user_form.is_valid() and user_profile_form.is_valid():
            auth_user_form.save()

            profile = user_profile_form.save(commit=False)
            current_user = User.objects.get(username=auth_user_form.cleaned_data.get('username'))
            profile.user_id = current_user.id
            profile.save()

            username = auth_user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("login")
    else:
        auth_user_form = AuthUserForm()
        user_profile_form = UserProfile()
    return render(request, 'User/register.html', {
        "auth_user_form": auth_user_form,
        "user_profile_form": user_profile_form,
    })


def profile_update(request):
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=request.user.id).first()
    if request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        auth_user_form = AuthUser(instance=user,   data=request.POST)
        if profile_form.is_valid() and auth_user_form.is_valid():

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            auth_user_form.save()

            return redirect("profile")

    return render(request, "User/profile.html", {
        "profile_form": ProfileForm(instance=profile),
        "auth_user_form": AuthUser(instance=user)
    })


