from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
        else:
            print(2)

    return render(request, 'User/register.html', {
        "form": UserCreationForm()
    })