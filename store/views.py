from django.http import request
from django.shortcuts import render
from .models import Product
# Create your views here.

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def checkout(request):
    """
    chechout function
    """
    context = {}
    return render(request,'store/checkout.html',context)



def store(request):
    products = Product.objects.all()
    """
    chechout function
    """
    context = {'products':products}
    return render(request,'store/store.html',context)

