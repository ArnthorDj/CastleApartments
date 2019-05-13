from django.shortcuts import render
from User.models import Profile
from django.contrib.auth.models import User


def index(request):
    #context = {'employees': Profile.objects.select_related('user').filter(user__is_staff=True)}

    #context2 = Profile.objects.select_related('user').all()
    #for project in context2:
    context = {'employees': User.objects.select_related('profile').filter(is_staff=True)}
    #for u in context['employees']:
        #print(u.first_name, u.profile.phone)

    return render(request, 'Employees/index.html', context)
