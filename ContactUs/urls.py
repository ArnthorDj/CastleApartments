from django.urls import path
from . import views


# url: /contact_us/
urlpatterns = [
    # contact_us/
    path("", views.contact_us, name='contact_us'),
]
