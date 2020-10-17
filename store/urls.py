from django.urls import path, include
from . import views
app_name='store'

urlpatterns = [
    path('',views.store,name="store"),
    path('checkout',views.checkout,name="checkout"),
    path('cart',views.cart,name="cart"),

]
