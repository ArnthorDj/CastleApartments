from django.shortcuts import render


def index(request):
    return render(request, 'Employees/index.html', context)
