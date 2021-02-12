from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from EcomApp.models import Setting
from Product.models import Product, Images, Category


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your username or password is invalid!')

    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request, 'user_login.html', context)


# Create your views here.
def user_logout(request):
    logout(request)
    return redirect('home')
