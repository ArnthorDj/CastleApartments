
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="pending_index"),
    path("pending_information/", views.info, name="pending_information_index")
]