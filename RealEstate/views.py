from django.shortcuts import render, redirect
from RealEstate.models import RealEstates, RealEstateImages
from django.http import HttpResponse
from PaymentInformation.forms.payment_information_forms import CreatePaymentform


def index(request):
    context = {'real_estates': RealEstates.objects.all().order_by('street')}
    images = {'images': RealEstateImages.objects.all()}
    return render(request, 'RealEstate/index.html', context)


def realEstateInformation(request):
    return render(request, 'RealEstateInformation/index.html')


def addRealEstatem(request):
    return HttpResponse("Hello from the index function within the AddRealEstate app!")


def addRealEstateCofirmation(request):
    return HttpResponse("Hello from the index function within the AddRealEstateConfirmation app!")


def payment_confirmation(request):
    return render(request, 'PaymentConfirmation/index.html')


def yourRealEstate(request):
    return HttpResponse("Hello from the index function within the YourRealEstate app!")

def payment_information(request):
    form = CreatePaymentform(data=request.POST)
    if form.is_valid():
        payment = form.save()
        return redirect('confirmation_index')
    else:
         form = CreatePaymentform()
    return render(request, 'PaymentInformation/index.html', {
         'form': form
         })