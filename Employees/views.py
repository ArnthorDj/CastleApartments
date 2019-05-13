from django.shortcuts import render
from User.models import Profile
from django.contrib.auth.models import User


def index(request):
    context = {'employees': User.objects.select_related('profile').filter(is_staff=True)}
    #for u in context['employees']:
        #print(u.first_name, u.profile.phone)

    return render(request, 'Employees/index.html', context)
