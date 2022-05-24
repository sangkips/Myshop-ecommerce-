from django.urls import path

from .views import home_view, order_product, order_checkout
   
urlpatterns = [
    path('', home_view, name='home'),
    path('products/', order_product, name='order-product'), 
    path('checkout/', order_checkout, name='checkout-page'), 
]
