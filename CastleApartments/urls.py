from django.urls import path, include


# Starting urls for the web page
urlpatterns = [
    path("", include("Home.urls")),
    path("home/", include("Home.urls")),
    path("user/", include("User.urls")),
    path("contact_us/", include("ContactUs.urls")),
    path("employees/", include("Employees.urls")),
    path("real_estate/", include("RealEstate.urls")),
]
