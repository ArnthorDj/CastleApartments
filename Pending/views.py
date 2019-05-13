from django.shortcuts import render


def pending(request):
    return render(request, 'Pending/index.html')


def pending_information(request):
    return render(request, 'PendingInformation/index.html')