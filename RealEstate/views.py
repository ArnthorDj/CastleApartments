from django.shortcuts import render, redirect, get_list_or_404
from RealEstate.models import RealEstates, RealEstateImages, ZipCodes
from RealEstate.forms.payment_information_form import CreatePaymentForm
from User.models import UserHistory, Profile, CreditCard
#from django.contrib.auth.models import User
from django.http import JsonResponse
import datetime
from django.db.models import Q
# from RealEstate.forms.add_real_estate_form import AddRealEstateForm


def index(request):
    #real_estates = {"real_estates":  RealEstates.objects.all()}
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        # zip_city = RealEstates.objects.all().values('zip_code__city')

        real_estate = [{
            'street': x.street,
            'zip_code_id': x.zip_code_id,
            'city': x.zip_code.city,
            'bedrooms': x.bedrooms,
            'bathrooms': x.bathrooms,
            'size': x.size,
            'type': x.type,
            'price': x.price,
            'main_image': x.main_image
            # 'main_image': x.main_image.image
        }
            for x in RealEstates.objects.filter(Q(street__icontains=search_filter) | Q(zip_code=search_filter) | Q(
                zip_code__city__icontains=search_filter))]
        return JsonResponse({'data': real_estate})

    return render(request, 'RealEstate/order.html', {
        "real_estates":  RealEstates.objects.all()
    })


def get_real_estate_by_id(request, id):

    if request.user.is_authenticated:
        if UserHistory.objects.filter(real_estate_id=id).all().count() == 0:
            user_his = UserHistory(real_estate_id=id, user=request.user)
            user_his.save()
        else:
            UserHistory.objects.filter(real_estate_id=id, user=request.user).update(date=datetime.date.today())

    return render(request, 'RealEstateInformation/index.html', {
        'real_estate': get_list_or_404(RealEstates, pk=id)[0],
        'employee': Profile.objects.select_related('user').get(user_id=20),
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


#def payment_confirmation(request):
#    return render(request, 'PaymentConfirmation/index.html')


# def yourRealEstate(request):
# return HttpResponse("Hello from the index function within the YourRealEstate app!")


def payment_information(request, id):
    credit_card = CreditCard.objects.get(user_id=request.user.profile.id)
    if request.method == "POST":
        credit_card_form = CreatePaymentForm(data=request.POST, instance=credit_card)
        if credit_card_form.is_valid():
            if CreditCard.objects.filter(user_id=request.user.profile.id).count() == 0:
                form2 = credit_card_form.save(commit=False)
                form2.user_id = request.user.profile.id
                form2.save()
            else:
                card_number = credit_card_form.cleaned_data.get('card_number')
                month = credit_card_form.cleaned_data.get('month')
                year = credit_card_form.cleaned_data.get('year')
                CreditCard.objects.filter(user_id=request.user.profile.id).update(card_number=card_number, month=month,
                                                                                  year=year)
            return redirect('payment_confirmation', id=id)
    else:
        credit_card_form = CreatePaymentForm(instance=credit_card)
    return render(request, 'PaymentInformation/index.html', {
        'credit_card_form': credit_card_form,
        'id': id
         })


def payment_confirmation(request, id):
    real_estate = RealEstates.objects.get(pk=id)
    return render(request, 'PaymentConfirmation/index.html', {
        'id': id,
        'real_estate': real_estate
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