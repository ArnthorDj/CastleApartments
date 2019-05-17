from django.shortcuts import render, redirect
from User.models import Profile, UserHistory
from User.forms.profile_form import ProfileForm, AuthUser
from django.contrib.auth.models import User
from User.forms.sign_up_form import UserProfile, AuthUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    """ Function that adds a new member """

    if request.method == "POST":
        auth_user_form = AuthUserForm(data=request.POST)
        user_profile_form = UserProfile(data=request.POST)

        if auth_user_form.is_valid() and user_profile_form.is_valid():

            # Gets the ssn-input from user.
            ssn = str(user_profile_form.cleaned_data.get('ssn'))

            # Removes '-' from input, if user has written ssn as such.
            ssn = ssn.replace('-', '')

            # Check to see if user input is valid, that is a number with length of 10 digits.
            if len(ssn) != 10 or not ssn.isdigit():
                messages.warning(request, f'Social Security Number (SSN) is not valid (must be 10 digit number)!')
                return redirect('register')

            # Saves new registration of member.
            auth_user_form.save()

            profile = user_profile_form.save(commit=False)
            current_user = User.objects.get(username=auth_user_form.cleaned_data.get('username'))
            profile.user_id = current_user.id
            profile.save()

            username = auth_user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            # Redirects user to login page, for the user to sign in.
            return redirect("login")
    else:
        auth_user_form = AuthUserForm()
        user_profile_form = UserProfile()

    # Renders the user to the same page with the form the user has to change to be valid.
    return render(request, 'User/register.html', {
        "auth_user_form": auth_user_form,
        "user_profile_form": user_profile_form,
    })


@login_required
def profile_update(request):
    """ Function so user has the availability to change/update
        already signed information about himself/herself. """

    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=request.user.id).first()

    if request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        auth_user_form = AuthUser(instance=user,   data=request.POST)
        if profile_form.is_valid() and auth_user_form.is_valid():

            # Gets the ssn-input from user.
            ssn = str(profile_form.cleaned_data.get('ssn'))

            # Removes '-' from input, if user has written ssn as such.
            ssn = ssn.replace('-', '')

            # Check to see if user input is valid, that is a number with length of 10 digits.
            if len(ssn) != 10 or not ssn.isdigit():
                messages.warning(request, f'SSN is not valid (10 numbers)!')
                return redirect('profile')

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            # Saves updated registration of member.
            auth_user_form.save()
            return redirect("profile")

    return render(request, "User/profile.html", {
        "profile_form": ProfileForm(instance=profile),
        "auth_user_form": AuthUser(instance=user)
    })


@login_required
def user_history(request):
    """ Gets user history. """

    # Gets the user history from the database
    user_history_real_estate = UserHistory.objects.prefetch_related('real_estate').filter(user_id=request.user)

    # Goes to the user history web page with the user history information
    return render(request, 'UserHistory/index.html', {
        'real_estates': user_history_real_estate
    })


@login_required
def delete_history(request):
    """ Deletes user history. """

    # Deletes all information in the database with user_id equal to the current users id
    UserHistory.objects.filter(user_id=request.user).delete()

    # Goes to the user history web page
    return redirect("user_history")
