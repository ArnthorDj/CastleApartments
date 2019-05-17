"""CastleApt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("Home.urls")),
    path("home/", include("Home.urls")),
    path("user/", include("User.urls")),
    path("contact_us/", include("ContactUs.urls")),
    path("employees/", include("Employees.urls")),
    path("real_estate/", include("RealEstate.urls")),
    #path("your_real_estate/", include("YourRealEstate.urls")),
    #path("pending/", include("Pending.urls")),

    # path('admin/', admin.site.urls),
    # path("login/", include("Login.urls")),
    # path("sign_up/", include("Signup.urls")),
    # path("payment_information/", include("PaymentInformation.urls")),
    # path("confirmation/", include("Confirmation.urls")),
    # path("real_estate_information/", include("RealEstateInformation.urls")),
    # path("add_real_estate/", include("AddRealEstate.urls")),
    # path("add_real_estate_confirmation/", include("AddRealEstateConfirmation.urls")),
]
