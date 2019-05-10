
from django.urls import path
from . import views

urlpatterns = [
    path("", views.pending, name="pending_index"),
    path("pending_info/", views.pending_information, name="pending_information_index")
]