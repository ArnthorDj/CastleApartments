from django.db import models
from django.contrib.auth.models import User
from RealEstate.models import RealEstates, ZipCodes


class Profile(models.Model):
    """ Here are information about user profile, which are stored in the User_Profile database table.
        Also retrieving information about zip-code (zip code, city, country) with foreign key reference. """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999, blank=True)
    street = models.CharField(max_length=99)
    phone = models.CharField(max_length=12)
    zip_code = models.ForeignKey(ZipCodes, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=11)


class Purchases(models.Model):
    """ Here are information about purchases made through the website,
        stored in the User_Purchases database table. """

    buyer = models.CharField(max_length=99)
    seller = models.CharField(max_length=99)
    real_estate = models.CharField(max_length=99)


class CreditCard(models.Model):
    """ Here are information stored for credit-card used by purchaser of real estate,
        stored in the User_CreditCard database table.
        Here are information retrieved as well from the User_Profile table with foreign key reference. """

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)


class UserHistory(models.Model):
    """ Here are information stored about user history, the real estates that user has viewed.
        Also retrieving information about user (user_id)
        and real estate (real_estate_id) with foreign key reference,
        as well as the date which the user viewed the real estate. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstates, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
