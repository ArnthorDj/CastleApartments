from django.shortcuts import render
from RealEstate.models import RealEstates, RealEstateImages
from django.http import HttpResponse


def realEstate(request):
    context = {'real_estates': RealEstates.objects.all().order_by('street')}
 #   images = {'images': RealEstateImages.objects.all()}
    return render(request, 'RealEstate/index.html', context)


def realEstateInformation(request):
    return render(request, 'RealEstateInformation/index.html')


def addRealEstatem(request):
    return HttpResponse("Hello from the index function within the AddRealEstate app!")


def addRealEstateCofirmation(request):
    return HttpResponse("Hello from the index function within the AddRealEstateConfirmation app!")


def buyConfirmation(request):
    return HttpResponse("Hello from the index function within the Confirmation app!")


def yourRealEstate(request):
    return HttpResponse("Hello from the index function within the YourRealEstate app!")

