from django.urls import path
from . import views

urlpatterns = [
    path("", views.pending, name="pending_index"),
    path("info/", views.pending_information, name="pending_information_index"),
    path("zip/", views.pending_zip, name="pending_zip"),
    path("street/", views.pending_street, name="pending_street"),
    path("size/", views.pending_size, name="pending_size"),
    path("price/", views.pending_price, name="pending_price"),
]
