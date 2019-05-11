from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from User.models import Profile
from User.forms.profile_form import ProfileForm, AuthUser
from django.contrib.auth.models import User
from User.forms.sign_up_form import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'User/register.html', {"form": form })




def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=request.user.id).first()
    if request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        auth_user_form = AuthUser(instance=user,   data=request.POST)
        if profile_form.is_valid() and auth_user_form.is_valid():

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            user = auth_user_form.save()

            return redirect("profile")

    return render(request, "User/profile.html", {
        "profile_form": ProfileForm(instance=profile),
        "auth_user_form": AuthUser(instance=user)
    })


