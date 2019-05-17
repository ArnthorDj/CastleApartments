from django.db import models
from django.contrib.auth.models import User
from RealEstate.models import RealEstates, ZipCodes


class Profile(models.Model):
    """ Variables (columns) for the User_Profile table in database. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999, blank=True)
    street = models.CharField(max_length=99)
    phone = models.CharField(max_length=12)
    zip_code = models.ForeignKey(ZipCodes, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=11)


class Purchases(models.Model):
    """ Variables (columns) for the User_Purchases table in database. """
    buyer = models.CharField(max_length=99)
    seller = models.CharField(max_length=99)
    real_estate = models.CharField(max_length=99)


class CreditCard(models.Model):
    """ Variables (columns) for the User_CreditCard table in database. """
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)


class UserHistory(models.Model):
    """ Variables (columns) for the UserHistory table in database. """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstates, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
