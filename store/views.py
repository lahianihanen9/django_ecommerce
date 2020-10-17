from django.http import request
from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request,'store/cart.html')

def checkout(request):
    """
    chechout function
    """
    return render(request,'store/checkout.html')



def store(request):
    """
    chechout function
    """
    return render(request,'store/store.html')

