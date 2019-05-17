from django.shortcuts import render
from django.contrib.auth.models import User

# Gets all the users that are staff (is_staff = True) and sends them as context ('employees')
def index(request):
    context = {'employees': User.objects.select_related('profile').filter(is_staff=True).order_by('first_name')}
    return render(request, 'Employees/index.html', context)
