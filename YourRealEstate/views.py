from django.shortcuts import render
from django.http import HttpResponse


def your_real_estate(request):
    return HttpResponse("Hello from the index function within the YourRealEstate app!")


def add_real_estate(request):
    return render(request, "AddRealEstateConfirmation/index.html")


def add_real_estate_confirmation(request):
    return HttpResponse("Hello from the index function within the AddRealEstateConfirmation app!")