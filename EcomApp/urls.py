from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.About, name='about'),
    path('contact/', views.contact, name='contact_dat'),
    path('product/<int:id>/', views.product_single, name='product_single'),
    path('product/<int:id>/<slug:slug>/', views.category_product, name='category_product'),
    path('search/', views.SearchView, name='SearchView'),
]