from django.db import models
from django import forms

MONTHS = {
    'january':('01'),
    'febuary':('02'),
    'mars':('03'),
    'april':('04'),
    'may':('05'),
    'june':('06'),
    'july':('07'),
    'august':('08'),
    'september':('09'),
    'october':('10'),
    'november':('11'),
    'december':('12')
    }





class CreditCard(models.Model):
    card_number = models.CharField(max_length=16)
    month = forms.CharField(max_length=30)
    year = models.CharField(max_length=4)
    cvc = models.CharField(max_length=3)

    def __str__(self):
        return "Card Number: {}\nMonth: {}\nYear: {}\nCVC: {}".format(self.card_number, self.month, self.year, self.cvc)
