from django.shortcuts import render
from RealEstate.models import RealEstates
from django.http import JsonResponse
from django.db.models import Q


def index(request):
    #real_estates = {"real_estates":  RealEstates.objects.all()}
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        # zip_city = RealEstates.objects.all().values('zip_code__city')

        real_estate = [{
            'id': x.id,
            'street': x.street,
            'zip_code_id': x.zip_code_id,
            'city': x.zip_code.city,
            'bedrooms': x.bedrooms,
            'bathrooms': x.bathrooms,
            'size': x.size,
            'type': x.type,
            'price': x.price,
            'main_image': x.main_image
            # 'main_image': x.main_image.image
        }
            for x in RealEstates.objects.filter((Q(street__icontains=search_filter) | Q(zip_code=search_filter) | Q(
                zip_code__city__icontains=search_filter)) & Q(on_sale=True))]
        return JsonResponse({'data': real_estate})

    return render(request, 'Home/index.html', {
        "real_estates":  RealEstates.objects.filter(on_sale=True)[:6]})


