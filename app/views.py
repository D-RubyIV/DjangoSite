from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(requests):
    products = Product.objects.all()
    context = {'products': products}
    return render(requests, 'app/home.html', context)
