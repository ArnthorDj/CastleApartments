from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def pending(request):
    return render(request, 'Pending/index.html')

def pending_information(request):
    return render(request, 'PendingInformation/index.html')