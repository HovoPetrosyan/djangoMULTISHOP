from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.urls import reverse
from django.contrib import messages
from OrderApp.models import ShopCart
from EcomApp.models import Setting, ContactMessage, ContactForm
from Product.models import Product, Images, Category, Comment

from EcomApp.forms import SearchForm


# Create your views here.
def home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price * p.qty
    sliding_images = Product.objects.all().order_by('id')[:3]
    latest_products = Product.objects.all().order_by('-id')
    products = Product.objects.all()

    context = {
               'sliding_images': sliding_images,
               'latest_products': latest_products,
               'products': products,
               'cart_product': cart_product,
               'total_amount': total_amount,
               }
    return render(request, 'home.html', context)


def About(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # messages.success(request, 'Your message has been sent')
            print(request.META)
            return HttpResponseRedirect(reverse('contact_dat'))

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    category = Category.objects.all()
    context = {
        'setting': setting,
        'form': form,
        'category': category,
    }
    return render(request, 'contact_form.html', context)


def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.objects.filter(
                title__icontains=query)
        category = Category.objects.all()
        sliding_images = Product.objects.all().order_by('id')[:3]
        setting = Setting.objects.get(pk=1)
        context = {
            'category': category,
            'query': query,
            'product_cat': products,
            'sliding_images': sliding_images,
            'setting': setting,
        }
        return render(request, 'category_products.html', context)

    return HttpResponseRedirect('category_product')


def product_single(request, id):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    single_product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:4]
    comment_show = Comment.objects.filter(product_id=id, status='True')[:3]
    context = {
        'category': category,
        'setting': setting,
        'single_product': single_product,
        'images': images,
        'products': products,
        'comment_show': comment_show,
    }
    return render(request, 'product-single.html', context)


def category_product(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:2]
    product_cat = Product.objects.filter(category_id=id)
    context = {
        'category': category,
        'setting': setting,
        'product_cat': product_cat,
        'sliding_images': sliding_images,
    }
    return render(request, 'category_products.html', context)
