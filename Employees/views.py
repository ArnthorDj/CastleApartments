from django.shortcuts import render
from Employees.models import Employees


def index(request):
    context = {'employees': Employees.objects.all().order_by('first_name')}
    return render(request, 'Employees/index.html', context)
