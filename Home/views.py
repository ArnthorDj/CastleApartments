from django.shortcuts import render
from RealEstate.models import RealEstates

def index(request):
    real_estate = RealEstates.objects.all().order_by('city')[:6]
    return render(request, 'Home/index.html',
                  { "real_estates": real_estate }
                  )
