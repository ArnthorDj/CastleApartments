from django.shortcuts import render
from User.models import Profile


def index(request):
    context = {'employees': Profile.objects.all().order_by('user__first_name')}
    return render(request, 'Employees/index.html', context)
