from django.shortcuts import render
from django.http import HttpResponse
from YourRealEstate.forms.add_real_estate_form import AddRealEstateForm


def your_real_estate(request):
    return render(request, "YourRealEstate/index.html")


def add_real_estate(request):
    form = AddRealEstateForm(data=request.POST)
    if form.is_valid():
        new_real_estate = form.save()
        return redirect('confirmation_index')
    else:
        form = AddRealEstateForm()
    return render(request, 'AddRealEstate/index.html', {
        'form': form
    })


def add_real_estate_confirmation(request):
    return render(request, "AddRealEstateConfirmation/index.html")
