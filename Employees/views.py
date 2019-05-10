from django.shortcuts import render
from User.models import Profile


def index(request):
    context = {'employees': Profile.objects.filter(user__is_staff=True)}
    return render(request, 'Employees/index.html', context)
