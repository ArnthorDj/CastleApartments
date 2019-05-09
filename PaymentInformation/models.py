from django.db import models
from User.models import Profile


class CreditCard(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
