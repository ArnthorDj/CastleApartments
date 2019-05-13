from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999, blank=True)
    phone = models.CharField(max_length=12)


class Purchases(models.Model):
    buyer = models.CharField(max_length=99)
    seller = models.CharField(max_length=99)
    real_estate = models.CharField(max_length=99)




