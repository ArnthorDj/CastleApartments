from django.db import models
from django.contrib.auth.models import User
from User.models import Profile

class RealEstates(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=99)
    zip_code = models.CharField(max_length=3)
    size = models.CharField(max_length=10)
    bedrooms = models.CharField(max_length=2)
    bathrooms = models.CharField(max_length=2)
    type = models.CharField(max_length=99)
    price = models.CharField(max_length=999)
    on_sale = models.BooleanField()
    more_info = models.CharField(max_length=999)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    main_image = models.CharField(max_length=999)


class RealEstateImages(models.Model):
    real_estate = models.ForeignKey(RealEstates, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)

class CreditCard(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)




