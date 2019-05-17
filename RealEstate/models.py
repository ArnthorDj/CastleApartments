from django.db import models
from django.contrib.auth.models import User


class ZipCodes(models.Model):
    """ Here are information about zip codes, which are stored in the Real_Estate_zip_codes table."""

    zip_code = models.CharField(max_length=3, primary_key=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class RealEstates(models.Model):
    """ Here are information about the real estate, which are stored in Real_Estate_real_estates table.
        Alse retrieving information about zip-code (zip code, city, country) and the Employee (User)
        that created the real estate with foreign key reference"""

    street = models.CharField(max_length=255)
    zip_code = models.ForeignKey(ZipCodes, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    bedrooms = models.CharField(max_length=2)
    bathrooms = models.CharField(max_length=2)
    type = models.CharField(max_length=99)
    price = models.CharField(max_length=999)
    on_sale = models.BooleanField()
    more_info = models.CharField(max_length=999)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    main_image = models.CharField(
        max_length=999,
        default="https://image.shutterstock.com/image-vector/simple-house-icon-white-flat-260nw-1086201605.jpg")


class RealEstateImages(models.Model):
    """ Hera are information about real estate images, which are stored in the Real_Estate_real_estate_images.
        Also retrieving information about the real estate (Real_Estate_real_estates) that 'owns' the images
        with foreign key reference """

    real_estate = models.ForeignKey(RealEstates, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)
    image2 = models.CharField(max_length=9999)
    image3 = models.CharField(max_length=9999)
    image4 = models.CharField(max_length=9999)
    image5 = models.CharField(max_length=9999)
    image6 = models.CharField(max_length=9999)
