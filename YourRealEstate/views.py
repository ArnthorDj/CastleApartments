from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def your_real_estate(request):
    return render(request, "YourRealEstate/index.html")

def add_real_estate(request):
    return render(request, "AddRealEstateConfirmation/index.html")

def add_real_estate_confirmation(request):
    return HttpResponse("Hello from the index function within the AddRealEstateConfirmation app!")