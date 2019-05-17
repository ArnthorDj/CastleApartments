from django.shortcuts import render


def contact_us(request):
    """ Goes to 'Contact Us' html page. """

    return render(request, 'ContactUs/index.html')
