from django.shortcuts import render, redirect, get_list_or_404
from RealEstate.models import RealEstates, RealEstateImages, ZipCodes
from RealEstate.forms.payment_information_form import CreatePaymentForm
from django.http import JsonResponse
# from RealEstate.forms.add_real_estate_form import AddRealEstateForm


def index(request):
    #real_estates = {"real_estates":  RealEstates.objects.all()}
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        real_estate = [{
            'street': x.street,
            'city': x.city,
            'zip_code': x.zip_code,
            'bedrooms': x.bedrooms,
            'bathrooms': x.bathrooms,
            'size': x.size,
            'type': x.type,
            'price': x.price
            # 'main_image': x.main_image.image
        } for x in RealEstates.objects.filter(street__icontains=search_filter)]
        return JsonResponse({'data':real_estate})
    return render(request, 'RealEstate/index.html', {
        "real_estates":  RealEstates.objects.all()
    })


#def real_estate_information(request):
#    return render(request, 'RealEstateInformation/index.html')


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



# def search(request):
#     if 'search_filter' in request.GET:
#         search_filter = request.GET['search_filter']
#         real_estates = list(RealEstates.objects.filter(street__icontains=search_filter).values())
#         return JsonResponse({'data':real_estates})
#     context = {'real_estate': RealEstates.objects.all().order_by('street')}
#     return render(request, 'RealEstate/index.html', context)