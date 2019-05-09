from django.shortcuts import render, redirect
from PaymentInformation.forms.payment_information_forms import CreatePaymentform
# Create your views here.


def index(request):

    return render(request, 'PaymentInformation/index.html')


#def payment_information(request):
 #   if request.method == 'POST':
  #      form = CreatePaymentform(data=request.POST)
  #      if form.is_valid():
   #         payment = form.save()
   #         return redirect('confirmation_index')
   # else:
   #     form = CreatePaymentform()
   # return render(request, 'PaymentInformation/index.html', {
   #     'form': form
   # })



def payment_information(request):
    form = CreatePaymentform(data=request.POST)
    if form.is_valid():
        payment = form.save()
        return redirect('confirmation_index')
    else:
         form = CreatePaymentform()
    return render(request, 'PaymentInformation/index.html', {
         'form': form
         })
