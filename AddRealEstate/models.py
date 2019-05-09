from django.db import models
from django import forms



class NewRealEstate(models.Model):
    #id = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=99)
    zip_code = models.CharField(max_length=3)
    size = models.CharField(max_length=10)
    bedrooms = models.CharField(max_length=2)
    type = models.CharField(max_length=99)
    price = models.CharField(max_length=999)
    on_sale = models.BooleanField()
    seller_id = models.IntegerField()

    def __str__(self):
        return "Street: {}\nCity: {}\nZip Code: {}\nSize: {}\nBedrooms: {}\nType: {}\nPrice: {}".format(self.street, self.city, self.zip_code, self.size, self.bedrooms, self.type, self.price)

