from django.shortcuts import render, redirect
from AddRealEstate.forms.add_real_estate_form import AddRealEstateForm

# Create your views here.

#def index(request):
 #   form = AddRealEstateForm(data=request.POST)
  #  return render(request, 'AddRealEstate/index.html')

#def index(request):
#    form = AddRealEstateForm(data=request.POST)
#    if form.is_valid():
#        new_real_estate = form.save()
#        return redirect('confirmation_index')
#    else:
#        form = AddRealEstateForm()
#    return render(request, 'AddRealEstate/index.html', {
#        'form': form
#    })