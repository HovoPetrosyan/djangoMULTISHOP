from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect, reverse

from EcomApp.models import Setting, ContactMessage, ContactForm
from Product.models import Category, Product, Images

from OrderApp.models import ShopCart, ShopingCartForm

from django.contrib import messages


def add_to_shopping_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = ShopCart.objects.filter(product_id=id,
                                       user_id=current_user.id)
    if checking:
        control = 1
    else:
        control = 0

    if request.method == "POST":
        form = ShopingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.filter(
                    product_id=id,
                    user_id=current_user.id
                )
                data.qty += form.cleaned_data['qty']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.qty = form.cleaned_data['qty']
                data.save()
        messages.success(request, 'Your Product  has been added!')
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.filter(
                product_id=id,
                user_id=current_user.id
            )
            data.qty += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.qty = 1
            data.save()
        messages.success(request, 'Your Product  has been added!')
        return HttpResponseRedirect(url)


def cart_details(request):
    current_user = request.user
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price * p.qty
    context = {
        'category': category,
        'setting': setting,
        'cart_product': cart_product,
        'total_amount': total_amount,
    }
    return render(request, 'cart_details.html', context)


def remove_from_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cart_product = ShopCart.objects.filter(id=id, user_id=current_user.id)
    cart_product.delete()
    messages.warning(request, 'Your Product  has been deleted!')
    return HttpResponseRedirect(url)

