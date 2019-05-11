from django.shortcuts import render
from User.models import Profile
from django.contrib.auth.models import User


def index(request):
    context = {'employees': Profile.objects.all().filter(user__is_staff=True)}
    for employee in context['employees']:
        print(employee.auth_user_password_set)
    print("THIS IS THE QUERYT")
    return render(request, 'Employees/index.html', context)
