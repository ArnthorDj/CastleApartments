from django.urls import path
from . import views


urlpatterns = [
    path("", views.your_real_estate, name="your_real_estate_index"),
    path("add/", views.add_real_estate, name="add_real_estate_index"),
    path("add/confirmation/", views.add_real_estate_confirmation, name="add_real_estate_confirmation_index"),
    path("zip/", views.your_real_estate_zip, name="your_real_estate_zip"),
    path("street/", views.your_real_estate_street, name="your_real_estate_street"),
    path("size/", views.your_real_estate_size, name="your_real_estate_size"),
    path("price/", views.your_real_estate_price, name="your_real_estate_price"),
    path("city/", views.your_real_estate_city, name="your_real_estate_city"),
]
