from django.urls import path
from . import views


# url: /employees/
urlpatterns = [
    # /employees/
    path("", views.index, name='employees_index'),
]
