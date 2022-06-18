from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def project(request):
    return render(request, 'Projectpage.html')


def contact(request):
    return render(request, 'Contactpage.html')


def cv(request):
    return render(request, 'Cvpage.html')


def home(request):
    return render(request, 'homepage.html')
