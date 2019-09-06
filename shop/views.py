from django.shortcuts import render
from django.http import HttpResponse
from . models import product
from math import ceil
# Create your views here.

def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nSlides =  n//4 + ceil(n/4 - n//4)
    params = {'no of slides': nSlides, 'range': range(1, nSlides),'product':products}

    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at Tracker")

def search(request):
    return HttpResponse("we are at search")

def prodView(request):
    return HttpResponse("we are at Product View")

def checkout(request):
    return HttpResponse("we are at Check Out")
