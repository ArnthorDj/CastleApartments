from django.shortcuts import render, redirect
from RealEstate.models import RealEstates
from RealEstate.forms.payment_information_form import CreatePaymentForm
# from RealEstate.forms.add_real_estate_form import AddRealEstateForm


def index(request):
    real_estates = {"real_estates":  RealEstates.objects.all()}
    return render(request, 'RealEstate/index.html',
                  real_estates
                  )


def real_estate_information(request):
    return render(request, 'RealEstateInformation/index.html')


# def addRealEstate(request):
# form = AddRealEstateForm(data=request.POST)
# if form.is_valid():
# new_real_estate = form.save()
# return redirect('confirmation_index')
# else:
# form = AddRealEstateForm()
# return render(request, 'AddRealEstate/index.html', {
# 'form': form
# })


# def addRealEstateCofirmation(request):
# return HttpResponse("Hello from the index function within the AddRealEstateConfirmation app!")


def payment_confirmation(request):
    return render(request, 'PaymentConfirmation/index.html')


# def yourRealEstate(request):
# return HttpResponse("Hello from the index function within the YourRealEstate app!")


def payment_information(request):
    form = CreatePaymentForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('confirmation_index')
    else:
        form = CreatePaymentForm()
    return render(request, 'PaymentInformation/index.html', {
         'form': form
         })
