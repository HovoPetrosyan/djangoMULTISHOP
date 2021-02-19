from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect, reverse

from EcomApp.models import Setting, ContactMessage, ContactForm
from Product.models import Category, Product, Images

from OrderApp.models import ShopCart, ShopingCartForm, OrderForm, OrderProduct, Order

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

from UserApp.models import UserProfile


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


@login_required(login_url='/user/login')
def orderCart(request):
    current_user = request.user
    shopping_cart = ShopCart.objects.filter(user_id=current_user.id)
    totalamount = 0
    for rs in shopping_cart:
        totalamount += rs.qty * rs.product.new_price
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.country = form.cleaned_data['country']
            data.transaction_id = form.cleaned_data['transaction_id']
            data.transaction_image = form.cleaned_data['transaction_image']
            data.user_id = current_user.id
            data.total = totalamount
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            for rs in shopping_cart:
                dat = OrderProduct()
                dat.order_id = data.id
                dat.product_id = rs.product_id
                dat.user_id = current_user.id
                dat.qty = rs.qty
                dat.price = rs.product.new_price
                dat.amount = rs.amount
                dat.save()

                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.qty
                product.save()
            ShopCart.objects.filter(user_id=current_user.id).delete()
            messages.success(request, 'Your order has been completed!')
            category = Category.objects.all()
            setting = Setting.objects.get(id=1)
            context = {
                'ordercode': ordercode,
                'category': category,
                'setting': setting,
            }
            return render(request, 'order_completed.html', context)
        else:
            messages.warning(request, form.errors)

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    total_amount = 0
    for p in shopping_cart:
        total_amount += p.product.new_price * p.qty
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)

    context = {
        'shopping_cart': shopping_cart,
        'totalamount': totalamount,
        'profile': profile,
        'form': form,
        'category': category,
        'setting': setting,
        'total_amount': total_amount,
    }
    return render(request, 'order_form.html', context)


def order_showing(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'orders': orders,
    }

    return render(request, 'user_order.html', context)


@login_required(login_url='/user/login')
def user_order_details(request, id):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    order_products = OrderProduct.objects.filter(order_id=id)
    context = {
        'order': order,
        'order_products': order_products,
        'category': category,
        'setting': setting,
    }
    return render(request, 'user_order_details.html', context)


def order_product_showing(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'order_product': order_product,
    }

    return render(request, 'order_product_list.html', context)


@login_required(login_url='/user/login')
def user_productorder_details(request, id, oid):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    order_products = OrderProduct.objects.get(user_id=current_user.id, id=id)
    context = {

        'order': order,
        'order_products': order_products,
        'category': category,
        'setting': setting,
    }
    return render(request, 'user_order_product_details.html', context)

