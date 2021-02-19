from django.urls import path
from OrderApp.views import (add_to_shopping_cart,
                            cart_details,
                            remove_from_cart,
                            orderCart,
                            order_showing,
                            order_product_showing,
                            user_order_details,
                            user_productorder_details)

urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_shopping_cart, name='add_to_shopping_cart'),
    path('cart_details/', cart_details, name='cart_details'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('order_cart/', orderCart, name='order_cart'),
    path('orderlist/', order_showing, name='orderlist'),
    path('orderproduct/', order_product_showing, name='orderproduct'),
    path('orderdetails/<int:id>/', user_order_details, name='orderdetails'),
    path('order_product_details/<int:id>/<int:oid>/', user_productorder_details, name='order_product_details'),
]
