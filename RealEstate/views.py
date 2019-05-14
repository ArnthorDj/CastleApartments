from django.shortcuts import render, redirect, get_list_or_404
from RealEstate.models import RealEstates, RealEstateImages, ZipCodes
from RealEstate.forms.payment_information_form import CreatePaymentForm
from django.http import JsonResponse
# from RealEstate.forms.add_real_estate_form import AddRealEstateForm


def index(request):
    #real_estates = {"real_estates":  RealEstates.objects.all()}
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        zip_city = RealEstates.objects.filter().values('zip_code__city')

        real_estate = [{
            'street': x.street,
            'zip_code_id': x.zip_code_id,
            'city': zip_city,
            'bedrooms': x.bedrooms,
            'bathrooms': x.bathrooms,
            'size': x.size,
            'type': x.type,
            'price': x.price,
            # 'main_image': x.main_image.image
        }
            for x in RealEstates.objects.filter(street__icontains=search_filter)]
        return JsonResponse({'data': real_estate})

    return render(request, 'RealEstate/index.html', {
        "real_estates":  RealEstates.objects.all()
    })


def get_real_estate_by_id(request, id):
    return render(request, 'RealEstateInformation/index.html', {
        'real_estate': get_list_or_404(RealEstates, pk=id),
        'images': get_list_or_404(RealEstateImages, real_estate_id=id)
    })

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



def real_estate_zip(request):
    return render(request, 'RealEstate/zip.html', {"real_estates": RealEstates.objects.all().order_by("zip_code")})


def real_estate_street(request):
    return render(request, 'RealEstate/street.html', {"real_estates": RealEstates.objects.all().order_by("street")})


def real_estate_size(request):
    return render(request, 'RealEstate/size.html', {"real_estates": RealEstates.objects.all().order_by("size")})


def real_estate_price(request):
    return render(request, 'RealEstate/price.html', {"real_estates": RealEstates.objects.all().order_by("price")})


def real_estate_city(request):
    return render(request, 'RealEstate/city.html', {"real_estates": RealEstates.objects.all().order_by("zip_code__city")})


def real_estate_bathrooms(request):
    return render(request, 'RealEstate/bathrooms.html', {"real_estates": RealEstates.objects.all().order_by("bathrooms")})


def real_estate_bedrooms(request):
    return render(request, 'RealEstate/bedrooms.html', {"real_estates": RealEstates.objects.all().order_by("bedrooms")})