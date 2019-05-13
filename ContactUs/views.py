from django.shortcuts import render


def contact_us(request):
    return render(request, 'ContactUs/index.html')
