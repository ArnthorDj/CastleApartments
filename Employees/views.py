from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    context = {'employees': User.objects.select_related('profile').filter(is_staff=True).order_by('first_name')}
    return render(request, 'Employees/index.html', context)
