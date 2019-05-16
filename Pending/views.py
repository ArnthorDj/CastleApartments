from django.shortcuts import render
from RealEstate.models import RealEstates, RealEstateImages


def pending(request):
    return render(request, 'Pending/index.html', {"real_estates": RealEstates.objects.all()})


def pending_information(request):
    return render(request, 'PendingInformation/index.html')


def pending_zip(request):
    return render(request, 'Pending/index.html', {"real_estates": RealEstates.objects.all().order_by("zip_code")})


def pending_street(request):
    return render(request, 'Pending/index.html', {"real_estates": RealEstates.objects.all().order_by("zip_code__city")})


def pending_size(request):
    return render(request, 'Pending/index.html', {"real_estates": RealEstates.objects.all().order_by("size")})


def pending_price(request):
    return render(request, 'Pending/index.html', {"real_estates": RealEstates.objects.all().order_by("price")})


def pending_city(request):
    return render(request, 'Pending/index.html', {"real_estates": RealEstates.objects.all().order_by("zip_code__city")})

