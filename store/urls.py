from django.urls import path, include
from . import views
app_name='store'

urlpatterns = [
    path('',views.store),
    path('checkout',views.checkout),
    path('cart',views.cart),

]
