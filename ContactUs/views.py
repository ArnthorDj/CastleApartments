from django.shortcuts import render

# Goes to contact us html
def contact_us(request):
    return render(request, 'ContactUs/index.html')
