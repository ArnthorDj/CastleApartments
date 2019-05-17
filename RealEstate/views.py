from django.shortcuts import render, redirect, get_list_or_404
from RealEstate.models import RealEstates, RealEstateImages
from RealEstate.forms.payment_information_form import CreatePaymentForm
from User.models import UserHistory, Profile, CreditCard, Purchases
from django.http import JsonResponse
import datetime
from django.db.models import Q
from RealEstate.forms.add_real_estate_form import AddRealEstateForm, AddRealEstateImage
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    """ Search function based on the Canvas instruction video,
        and adapted to the function of Castle Apartments website. """

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']

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
            'main_image': x.main_image,
            'country': x.zip_code.country
        }
            for x in RealEstates.objects.filter((Q(street__icontains=search_filter) | Q(zip_code=search_filter) | Q(
                zip_code__city__icontains=search_filter)) & Q(on_sale=True))]
        return JsonResponse({'data': real_estate})

    return render(request, 'RealEstate/order.html', {
        "real_estates":  RealEstates.objects.filter(on_sale=True)
    })


def get_real_estate_by_id(request, id):
    """ Function that gets specific real estate (by id). """

    # Get the specific real estate or throw 404 error.
    real_estate = get_list_or_404(RealEstates, pk=id)[0]

    # If the specific real estate is not on sale, the user is redirected to the url: /real_estate/
    if not real_estate.on_sale:
        return redirect('real_estate')

    # Checks if the user is logged in.
    # If he is logged in, checks if he has already had a look at this specific real estate.
    if request.user.is_authenticated:
        if UserHistory.objects.filter(real_estate_id=id, user_id=request.user).all().count() == 0:

            # Adds the real estate to user history.
            user_his = UserHistory(real_estate_id=id, user=request.user)
            user_his.save()

        else:
            # updates the date in user history.
            UserHistory.objects.filter(real_estate_id=id, user=request.user).update(date=datetime.date.today())

    # Gets the specific real estate images.
    placeholder = RealEstateImages.objects.get(real_estate_id=id)

    # Sets the images in a more convenient data storage.
    images = [placeholder.image, placeholder.image2, placeholder.image3, placeholder.image4, placeholder.image5, placeholder.image6]

    # Goes to the real estate information web page,
    # with the necessary information to display on the RealEstateInformation page.
    return render(request, 'RealEstateInformation/index.html', {
        'real_estate': real_estate,
        'employee': Profile.objects.select_related('user').get(user_id=real_estate.employee_id),
        'images': images
    })


@login_required
def add_real_estate(request):
    """ Adds the newly registered real estate to the database. """

    # If the current user is not staff, throw him to homepage url: /home/
    if not request.user.is_staff:
        return redirect('home_index')

    if request.method == "POST":
        new_real_estate_form = AddRealEstateForm(data=request.POST)
        if new_real_estate_form.is_valid():
            new_real_estate_form2 = new_real_estate_form.save(commit=False)

            # Sets the real estate on sale.
            new_real_estate_form2.on_sale = True

            # Sets the employee_id to current user (that is employee) that is signed in.
            new_real_estate_form2.employee_id = request.user.id
            new_real_estate_form2.save()

            # Redirects the user to the next step, to add images to the specific real estate.
            return redirect('real_estate_image', id=new_real_estate_form2.id)
    else:
        new_real_estate_form = AddRealEstateForm()

    # Goes to add real estate page with the form that the user needs to fill out.
    return render(request, 'AddRealEstate/index.html', {
        'form': new_real_estate_form
    })


@login_required
def update_real_estate(request, id):
    """ Updates information about specific real estate in the database. """

    # If the current user is not staff, throw him to homepage url: /home/
    if not request.user.is_staff:
        return redirect('home_index')

    # Gets the real estate to update.
    real_estate = RealEstates.objects.get(pk=id)

    # If the real estate is not on sale then throw the user to real_estate url: /real_estate/
    if not real_estate.on_sale:
        return redirect('real_estate')

    if request.method == "POST":
        real_estate_form = AddRealEstateForm(data=request.POST, instance=real_estate)
        if real_estate_form.is_valid():

            # Gets the user input and puts them in a variable.
            street = real_estate.street
            type = real_estate.type
            more_info = real_estate.more_info
            main_image = real_estate.main_image
            price = real_estate.price
            size = real_estate.size
            bedrooms = real_estate.bedrooms
            bathrooms = real_estate.bathrooms

            # Updates the specific real estate with the given user information.
            RealEstates.objects.filter(id=id).update(street=street, type=type, more_info=more_info,
                                                     main_image=main_image, price=price, size=size,
                                                     bedrooms=bedrooms, bathrooms=bathrooms)

            # Redirects the user to the next step (update the current real estate images).
            return redirect('real_estate_image', id=id)
    else:
        real_estate_form = AddRealEstateForm(instance=real_estate)

    # Goes to the add_real_estate page with a form that has the current information
    # of the real estate (if there are any).
    return render(request, 'AddRealEstate/index.html', {
        'form': real_estate_form
    })


@login_required
def add_real_estate_images(request, id):
    """ Adds or updates images for specific real estate. """

    # If the current user is not staff, throws the user to real_estate url: /real_estate/
    if not request.user.is_staff:
        return redirect('real_estate')

    # Gets the images for specific real estate.
    images = RealEstateImages.objects.filter(real_estate_id=id)

    # Counts the images.
    image = images.count()

    # If there are no images then add new to RealEstateImages database table (else just update the images).
    if image == 0:
        real_estate_image_form = AddRealEstateImage(data=request.POST)

        # Sets the display images to "".
        images = ["", "",
                  "", "",
                  "", ""]

        if request.method == 'POST':
            if real_estate_image_form.is_valid():
                form2 = real_estate_image_form.save(commit=False)

                # Sets the real_estate_id foreign_key to the current real_estate_id.
                form2.real_estate_id = id
                form2.save()

                # Sets the images that the user inputs to the variables.
                pic1 = real_estate_image_form.cleaned_data.get('image')
                pic2 = real_estate_image_form.cleaned_data.get('image2')
                pic3 = real_estate_image_form.cleaned_data.get('image3')
                pic4 = real_estate_image_form.cleaned_data.get('image4')
                pic5 = real_estate_image_form.cleaned_data.get('image5')
                pic6 = real_estate_image_form.cleaned_data.get('image6')

                # Sets the display images to the user input.
                images = [pic1, pic2,
                          pic4, pic3,
                          pic5, pic6]

    # If there are images for the specific real estate, then update them.
    else:
        if request.method == 'POST':
            real_estate_image_form = AddRealEstateImage(data=request.POST, instance=images[0])

            if real_estate_image_form.is_valid():

                # Sets the images that the user input to variables.
                pic1 = real_estate_image_form.cleaned_data.get('image')
                pic2 = real_estate_image_form.cleaned_data.get('image2')
                pic3 = real_estate_image_form.cleaned_data.get('image3')
                pic4 = real_estate_image_form.cleaned_data.get('image4')
                pic5 = real_estate_image_form.cleaned_data.get('image5')
                pic6 = real_estate_image_form.cleaned_data.get('image6')

                # Updates the specific real_estate_image with the input from the user.
                RealEstateImages.objects.filter(real_estate_id=id).update(image=pic1, image2=pic2, image3=pic3,
                                                                          image4=pic4, image5=pic5, image6=pic6)

                # Sets the display images to the users input.
                images = [pic1, pic2,
                          pic4, pic3,
                          pic5, pic6]

        else:
            real_estate_image_form = AddRealEstateImage(instance=images[0])

            # Sets the display images to what is already in the database.
            images = [images[0].image, images[0].image2,
                      images[0].image3, images[0].image4,
                      images[0].image5, images[0].image6]

    # Goes to the add/update real_estate images with a form that has current information of the real estate images
    # and displays the images to the page (if there are any images already in the database).
    return render(request, 'AddRealEstate/images.html', {
        'image_form': real_estate_image_form,
        'images': images,
        'id': id
    })


@login_required
def payment_information(request, id):
    """ Gets the credit card information. """

    # If the user is staff, throws the user to the url: /real_estate/info/:id/
    if request.user.is_staff:
        return redirect('real_estate_information', id=id)

    # If there is not any credit card information in the database for a user, then create one.
    if CreditCard.objects.filter(user_id=request.user.profile.id).count() == 0:
        if request.method == "POST":
            credit_card_form = CreatePaymentForm(data=request.POST)
            if credit_card_form.is_valid():

                # Gets the user input about the credit card and puts it into variables.
                credit_card_number = str(credit_card_form.cleaned_data.get('card_number'))

                # Gets the credit card expiration date.
                credit_card_month = int(credit_card_form.cleaned_data.get('month'))
                credit_card_year = int(credit_card_form.cleaned_data.get('year'))

                # Checks if the credit card number is valid or not.
                if not credit_card_number.isdigit() or len(credit_card_number) != 16:

                    # Throws a message on the screen showing the error for the given credit card number.
                    messages.warning(request, f'Card number is not valid (16 numbers)!')
                    return redirect('payment_information_index', id=id)

                # Gets the current year and month given by user.
                month = int(datetime.datetime.now().month)
                year = int(datetime.datetime.now().year)

                # Checks if the credit card expiration date is valid or not.
                if credit_card_month < month and credit_card_year == year or credit_card_year < year:

                    # Throws a message on the screen, showing the error for the expiration date given.
                    messages.warning(request, f'Card is expired!')
                    return redirect('payment_information_index', id=id)

                credit_card_form2 = credit_card_form.save(commit=False)

                # Sets the user_id foreign_key to the current user id.
                credit_card_form2.user_id = request.user.profile.id
                credit_card_form2.save()

                # Goes to the next step (payment confirmation).
                return redirect('payment_confirmation', id=id)
        else:
            credit_card_form = CreatePaymentForm()

    # If there is a credit card information in the database for the current user,
    # then the credit card information is updated.
    else:

        # Gets the current credit card information for the user.
        credit_card = CreditCard.objects.get(user_id=request.user.profile.id)
        if request.method == "POST":
            credit_card_form = CreatePaymentForm(data=request.POST, instance=credit_card)
            if credit_card_form.is_valid():

                # Gets the user input about the credit card and puts it into variables.
                credit_card_number = str(credit_card_form.cleaned_data.get('card_number'))

                # Gets the credit card expiration date.
                credit_card_month = int(credit_card_form.cleaned_data.get('month'))
                credit_card_year = int(credit_card_form.cleaned_data.get('year'))

                # Checks if the credit card number is valid or not.
                if not credit_card_number.isdigit() or len(credit_card_number) < 16:

                    # Throws a message on the screen, showing the error in the given credit card number
                    messages.warning(request, f'Card number is not valid (16 numbers)!')
                    return redirect('payment_information_index', id=id)

                # Gets the current year and month.
                month = int(datetime.datetime.now().month)
                year = int(datetime.datetime.now().year)

                # Checks if the credit card expiration date is valid or not.
                if credit_card_month < month and credit_card_year == year or credit_card_year < year:

                    # Throws a message on the screen, showing the error for the given expiration date.
                    messages.warning(request, f'Card is expired!')
                    return redirect('payment_information_index', id=id)

                # Gets the user input about the credit card information and puts them into variables.
                card_number = credit_card_form.cleaned_data.get('card_number')
                month = credit_card_form.cleaned_data.get('month')
                year = credit_card_form.cleaned_data.get('year')

                # Updates the current credit card information for the specific user in the database.
                CreditCard.objects.filter(user_id=request.user.profile.id).update(card_number=card_number, month=month,
                                                                                  year=year)

                # Goes to the next step (payment confirmation).
                return redirect('payment_confirmation', id=id)
        else:
            credit_card_form = CreatePaymentForm(instance=credit_card)

    # Goes to the payment information page, with the credit card form and real_estate_id.
    return render(request, 'PaymentInformation/index.html', {
        'credit_card_form': credit_card_form,
        'id': id
         })


@login_required
def payment_confirmation(request, id):
    """  Goes to payment confirmation page with the right information given in earlier steps. """

    # Gets the real estate information.
    real_estate = RealEstates.objects.get(pk=id)

    # Gets the credit card information.
    credit_card = CreditCard.objects.get(user_id=request.user.profile.id)

    # Goes to payment confirmation page with:
    # id of the real estate
    # real estate information
    # The last 4 digits of credit card number
    return render(request, 'PaymentConfirmation/index.html', {
        'id': id,
        'real_estate': real_estate,
        'credit_card': str(credit_card.card_number)[12:]
    })


@login_required
def bought_real_estate(request, id):
    """ Inputs the purchase into the database. """

    # If the current user is staff, then throws the user to the url: /real_estate/
    if request.user.is_staff:
        return redirect('real_estate')

    # Gets the real estate information.
    real_estate = RealEstates.objects.filter(pk=id)

    # Set the real estate to 'not on sale'.
    real_estate.update(on_sale=False)

    # Sets the purchase information into the database (buyer, seller, real_estate).
    Purchases.objects.create(buyer=request.user.id, seller=real_estate[0].employee.id, real_estate=id)

    # Gives visual confirmation of purchase to the user.
    messages.success(request, f'House bought in {real_estate[0].street}, {real_estate[0].zip_code.zip_code} {real_estate[0].zip_code.city}, {real_estate[0].zip_code.country}!')

    # Throw the user (after purchase) to url: /real_estate/
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

