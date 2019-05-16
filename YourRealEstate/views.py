from django.shortcuts import render, redirect
from RealEstate.forms.add_real_estate_form import AddRealEstateForm
from RealEstate.models import RealEstates


def your_real_estate(request):
    return render(request, "YourRealEstate/index.html")


def add_real_estate(request):
    form = AddRealEstateForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('confirmation_index')
    else:
        form = AddRealEstateForm()
    return render(request, 'AddRealEstate/index.html', {
        'form': form
    })


def add_real_estate_confirmation(request):
    return render(request, "AddRealEstateConfirmation/index.html")


def your_real_estate_zip(request):
    return render(request, 'YourRealEstate/index.html', {"real_estates": RealEstates.objects.all().order_by("zip_code")})


def your_real_estate_street(request):
    return render(request, 'YourRealEstate/index.html', {"real_estates": RealEstates.objects.all().order_by("zip_code__city")})


def your_real_estate_size(request):
    return render(request, 'YourRealEstate/index.html', {"real_estates": RealEstates.objects.all().order_by("size")})


def your_real_estate_price(request):
    return render(request, 'YourRealEstate/index.html', {"real_estates": RealEstates.objects.all().order_by("price")})


def your_real_estate_city(request):
    return render(request, 'YourRealEstate/index.html', {"real_estates": RealEstates.objects.all().order_by("zip_code__city")})
