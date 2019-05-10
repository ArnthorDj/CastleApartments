from django.shortcuts import render
from django.http import HttpResponse


def your_real_estate(request):
    return render(request, "YourRealEstate/index.html")


def add_real_estate(request):
    return render(request, "AddRealEstate/index.html")


def add_real_estate_confirmation(request):
    return render(request, "AddRealEstateConfirmation/index.html")