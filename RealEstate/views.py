from django.shortcuts import render
from RealEstate.models import RealEstates, RealEstateImages


def index(request):
    context = {'real_estates': RealEstates.objects.all().order_by('street')}
    images = {'images': RealEstateImages.objects.all()}
    return render(request, 'RealEstate/index.html', context, images)


