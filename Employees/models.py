from django.db import models


class Employees(models.Model):
    profile_image = models.CharField(max_length=999)
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

