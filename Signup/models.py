from django.db import models


class Members(models.Model):
    profile_image = models.CharField(max_length=999)
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=12)
