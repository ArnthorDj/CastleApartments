from django.db import models
from Signup.models import Members


class RealEstates(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=99)
    zip_code = models.CharField(max_length=3)           # m.v. Ísland, þriggja stafa póstnúmer
    size = models.CharField(max_length=10)              # fermetrar
    bedrooms = models.CharField(max_length=2)           # fjöldi svefnherbergja
    type = models.CharField(max_length=99)              # týpa af fasteign (einbýlishús, blokk, höll...)
    price = models.CharField(max_length=999)
    on_sale = models.BooleanField()
    seller = models.ForeignKey(Members, on_delete=models.CASCADE)


class RealEstateImages(models.Model):
    house_id = models.ForeignKey(RealEstates, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)
