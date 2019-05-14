from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="real_estate"),
    path("info/<int:id>", views.get_real_estate_by_id, name="real_estate_information"),
    path("info/pay/", views.payment_information, name="payment_information_index"),
    path("info/pay/confirmation/", views.payment_confirmation, name="payment_confirmation"),
    # path("add/", views.addRealEstate, name="add_real_estate"),
    # path("add/confirmation/", views.addRealEstateConfirmation, name="add_real_estate_confirmation"),
    # path("your_real_estate/", views.yourRealEstate, name="your_real_estate"),
    path("zip/", views.real_estate_zip, name="real_estate_zip"),
    path("street/", views.real_estate_street, name="real_estate_street"),
    path("size/", views.real_estate_size, name="real_estate_size"),
    path("price/", views.real_estate_price, name="real_estate_price"),
    path("city/", views.real_estate_city, name="real_estate_city"),
]
