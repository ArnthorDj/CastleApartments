
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="payment_information_index"),
    path('payment_information', views.payment_information, name='payment_information')
]