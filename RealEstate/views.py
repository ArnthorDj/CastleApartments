from django.shortcuts import render, redirect, get_list_or_404
from RealEstate.models import RealEstates, RealEstateImages, ZipCodes
from RealEstate.forms.payment_information_form import CreatePaymentForm
from User.models import UserHistory, Profile, CreditCard, Purchases
#from django.contrib.auth.models import User
from django.http import JsonResponse
import datetime
from django.db.models import Q
from RealEstate.forms.add_real_estate_form import AddRealEstateForm, AddRealEstateImage
# from RealEstate.forms.add_real_estate_form import AddRealEstateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    #real_estates = {"real_estates":  RealEstates.objects.all()}
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        # zip_city = RealEstates.objects.all().values('zip_code__city')

        real_estate = [{
            'id': x.id,
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
            for x in RealEstates.objects.filter((Q(street__icontains=search_filter) | Q(zip_code=search_filter) | Q(
                zip_code__city__icontains=search_filter)) & Q(on_sale=True))]
        return JsonResponse({'data': real_estate})

    return render(request, 'RealEstate/order.html', {
        "real_estates":  RealEstates.objects.filter(on_sale=True)
    })


def get_real_estate_by_id(request, id):

    real_estate = get_list_or_404(RealEstates, pk=id)[0]


    if real_estate.on_sale == False:
        return redirect('real_estate')

    if request.user.is_authenticated:
        if UserHistory.objects.filter(real_estate_id=id).all().count() == 0:
            user_his = UserHistory(real_estate_id=id, user=request.user)
            user_his.save()
        else:
            UserHistory.objects.filter(real_estate_id=id, user=request.user).update(date=datetime.date.today())

    placeholder = RealEstateImages.objects.get(real_estate_id=id)

    images = [placeholder.image, placeholder.image2, placeholder.image3, placeholder.image4, placeholder.image5, placeholder.image6]

    return render(request, 'RealEstateInformation/index.html', {
        'real_estate': real_estate,
        'employee': Profile.objects.select_related('user').get(user_id=real_estate.employee_id),
        'images': images
    })

@login_required
def add_real_estate(request):
    if request.user.is_staff == False:
        return redirect('home_index')

    if request.method == "POST":
        new_real_estate_form = AddRealEstateForm(data=request.POST)
        if new_real_estate_form.is_valid():
            new_real_estate_form2 = new_real_estate_form.save(commit=False)
            new_real_estate_form2.on_sale = True
            new_real_estate_form2.save()

            return redirect('real_estate_image', id=new_real_estate_form2.id)
    else:
        new_real_estate_form = AddRealEstateForm()
    return render(request, 'AddRealEstate/index.html', {
        'form': new_real_estate_form
    })

@login_required
def update_real_estate(request, id):

    if request.user.is_staff == False:
        return redirect('home_index')

    real_estate = RealEstates.objects.get(pk=id)

    if real_estate.on_sale == False:
        return redirect('real_estate')

    if request.method == "POST":
        real_estate_form = AddRealEstateForm(data=request.POST, instance=real_estate)
        if real_estate_form.is_valid():

            street = real_estate.street
            type = real_estate.type
            more_info = real_estate.more_info
            main_image = real_estate.main_image
            price = real_estate.price
            size = real_estate.size
            bedrooms = real_estate.bedrooms
            bathrooms = real_estate.bathrooms

            RealEstates.objects.filter(pk=id).update(street=street, type=type, more_info=more_info,
                                                     main_image=main_image, price=price, size=size,
                                                     bedrooms=bedrooms, bathrooms=bathrooms)
            print("ID GIVEN:", id)
            print('GIVENGIVENVSDOLKFNAKSJDNFJIAKS')
            return redirect('real_estate_image', id=id)
    else:
        real_estate_form = AddRealEstateForm(instance=real_estate)
    return render(request, 'AddRealEstate/index.html', {
        'form': real_estate_form
    })


@login_required
def add_real_estate_images(request, id):

    if request.user.is_staff == False:
        return redirect('real_estate')

    images = RealEstateImages.objects.filter(real_estate_id=id)
    image = images.count()


    if image == 0:
        real_estate_image_form = AddRealEstateImage(data=request.POST)

        if request.method == 'POST':
            if real_estate_image_form.is_valid():
                form2 = real_estate_image_form.save(commit=False)
                form2.real_estate_id = id
                form2.save()

            return redirect('real_estate_image', id=id)

        images = ["", "",
                  "", "",
                  "", ""]

    else:
        if request.method == 'POST':
            real_estate_image_form = AddRealEstateImage(data=request.POST, instance=images[0])

            if real_estate_image_form.is_valid():
                pic1 = real_estate_image_form.cleaned_data.get('image')
                pic2 = real_estate_image_form.cleaned_data.get('image2')
                pic3 = real_estate_image_form.cleaned_data.get('image3')
                pic4 = real_estate_image_form.cleaned_data.get('image4')
                pic5 = real_estate_image_form.cleaned_data.get('image5')
                pic6 = real_estate_image_form.cleaned_data.get('image6')
                RealEstateImages.objects.filter(pk=images[0].id).update(image=pic1, image2=pic2, image3=pic3,
                                                                        image4=pic4, image5=pic5, image6=pic6)

            return redirect('real_estate_image', id=id)

        else:
            real_estate_image_form = AddRealEstateImage(instance=images[0])

        images = [images[0].image, images[0].image2,
                  images[0].image3, images[0].image4,
                  images[0].image5, images[0].image6]

    return render(request, 'AddRealEstate/images.html', {
        'image_form': real_estate_image_form,
        'images': images,
        'id': id
    })

# def addRealEstateCofirmation(request):
# return HttpResponse("Hello from the index function within the AddRealEstateConfirmation app!")


#def payment_confirmation(request):
#    return render(request, 'PaymentConfirmation/index.html')


# def yourRealEstate(request):
# return HttpResponse("Hello from the index function within the YourRealEstate app!")

@login_required
def payment_information(request, id):

    if request.user.is_staff == True:
        return redirect('real_estate_information', id=id)

    #CreditCard.objects.filter(user_id=request.user.profile.id).count() == 0:

    if CreditCard.objects.filter(user_id=request.user.profile.id).count() == 0:
        if request.method == "POST":
            credit_card_form = CreatePaymentForm(data=request.POST)
            if credit_card_form.is_valid():
                credit_card_number = str(credit_card_form.cleaned_data.get('card_number'))
                credit_card_month = int(credit_card_form.cleaned_data.get('month'))
                credit_card_year = int(credit_card_form.cleaned_data.get('year'))
                if not credit_card_number.isdigit() or len(credit_card_number) != 16:
                    messages.warning(request, f'Card number is not valid (16 numbers)!')
                    return redirect('payment_information_index', id=id)
                month = int(datetime.datetime.now().month)
                year = int(datetime.datetime.now().year)
                if credit_card_month < month and credit_card_year == year or credit_card_year < year:
                    messages.warning(request, f'Card is expired!')
                    return redirect('payment_information_index', id=id)

                credit_card_form2 = credit_card_form.save(commit=False)
                credit_card_form2.user_id = request.user.profile.id
                credit_card_form2.save()

                return redirect('payment_confirmation', id=id)
        else:
            credit_card_form = CreatePaymentForm()
    else:
        credit_card = CreditCard.objects.get(user_id=request.user.profile.id)
        if request.method == "POST":
            credit_card_form = CreatePaymentForm(data=request.POST, instance=credit_card)
            if credit_card_form.is_valid():
                credit_card_number = str(credit_card_form.cleaned_data.get('card_number'))
                credit_card_month = int(credit_card_form.cleaned_data.get('month'))
                credit_card_year = int(credit_card_form.cleaned_data.get('year'))
                if not credit_card_number.isdigit() or len(credit_card_number) < 16:
                    messages.warning(request, f'Card number is not valid (16 numbers)!')
                    return redirect('payment_information_index', id=id)
                month = int(datetime.datetime.now().month)
                year = int(datetime.datetime.now().year)
                if credit_card_month < month and credit_card_year == year or credit_card_year < year:
                    messages.warning(request, f'Card is expired!')
                    return redirect('payment_information_index', id=id)

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


@login_required
def payment_confirmation(request, id):
    real_estate = RealEstates.objects.get(pk=id)
    credit_card = CreditCard.objects.get(user_id=request.user.profile.id)
    return render(request, 'PaymentConfirmation/index.html', {
        'id': id,
        'real_estate': real_estate,
        'credit_card': str(credit_card.card_number)[12:]
    })


@login_required
def bought_real_estate(request, id):
    if request.user.is_staff == True:
        return redirect('real_estate')

    real_estate = RealEstates.objects.filter(pk=id)
    real_estate.update(on_sale=False)
    Purchases.objects.create(buyer=request.user.id, seller=real_estate[0].employee.id, real_estate=id)

    messages.success(request, f'House bought in {real_estate[0].street}, {real_estate[0].zip_code.zip_code} {real_estate[0].zip_code.city}, {real_estate[0].zip_code.country}!')

    return redirect('real_estate')


def real_estate_zip(request):
    return render(request, 'RealEstate/zip.html', {"real_estates": RealEstates.objects.filter(on_sale=True).order_by("zip_code")})


def real_estate_street(request):
    return render(request, 'RealEstate/street.html', {"real_estates": RealEstates.objects.filter(on_sale=True).order_by("street")})


def real_estate_size(request):
    return render(request, 'RealEstate/size.html', {"real_estates": RealEstates.objects.filter(on_sale=True).order_by("size")})


def real_estate_price(request):
    return render(request, 'RealEstate/price.html', {"real_estates": RealEstates.objects.filter(on_sale=True).order_by("price")})


def real_estate_city(request):
    return render(request, 'RealEstate/city.html', {"real_estates": RealEstates.objects.filter(on_sale=True).order_by("zip_code__city")})


def real_estate_bathrooms(request):
    return render(request, 'RealEstate/bathrooms.html', {"real_estates": RealEstates.objects.filter(on_sale=True).order_by("bathrooms")})


def real_estate_bedrooms(request):
    return render(request, 'RealEstate/bedrooms.html', {"real_estates": RealEstates.objects.filter(on_sale=True).order_by("bedrooms")})

