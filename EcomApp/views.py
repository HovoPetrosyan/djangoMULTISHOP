from django.shortcuts import render
from EcomApp.models import Setting
from Product.models import Product, Images, Category


# Create your views here.
def Home(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:3]
    latest_products = Product.objects.all().order_by('-id')
    products = Product.objects.all()

    context = {'category': category,
               'setting': setting,
               'sliding_images': sliding_images,
               'latest_products': latest_products,
               'products': products}
    return render(request, 'home.html', context)


def product_single(request, id):
    setting = Setting.objects.get(id=1)
    single_product=Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:4]
    context = {
        'setting': setting,
        'single_product': single_product,
        'images': images,
        'products': products,
    }
    return render(request, 'product-single.html', context)