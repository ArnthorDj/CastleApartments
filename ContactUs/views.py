from django.shortcuts import render


def contact_us(request):
    """ Goes to contact us html page """

    return render(request, 'ContactUs/index.html')
