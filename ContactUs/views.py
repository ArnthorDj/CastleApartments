from django.shortcuts import render


def contactUs(request):
    return render(request, 'ContactUs/index.html')
