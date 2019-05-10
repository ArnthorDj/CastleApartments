
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="real_estate"),
    path("info", views.realEstateInformation, name="real_estate_information"),
    path("info/pay/", views.payment_information, name="payment_information_index"),
    path("info/pay/confirmation/", views.payment_confirmation, name="payment_confirmation"),
    path("add/", views.addRealEstatem, name="add_real_estate"),
    path("add/confirmation/", views.addRealEstateCofirmation, name="add_real_estate_confirmation"),
    path("your_real_estate/", views.yourRealEstate, name="your_real_estate"),


]