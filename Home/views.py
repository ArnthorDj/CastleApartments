from django.shortcuts import render
from RealEstate.models import RealEstates

def index(request):
    real_estate = RealEstates.objects.all()[:5]
    return render(request, 'Home/index.html',
                  { "real_estates": real_estate }
                  )
