from django.urls import path
from OrderApp.views import add_to_shopping_cart, cart_details, remove_from_cart

urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_shopping_cart, name='add_to_shopping_cart'),
    path('cart_details/', cart_details, name='cart_details'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
]
