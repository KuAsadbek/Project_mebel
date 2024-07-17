import email
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import logout,login,authenticate
from product.models import Products
# from .models import Basket,CastumerUser
from django.contrib.auth.models import User

# def ProfilePage(request):
#     tom = Basket.objects.all()
#     return render(request,'user/profile.html',{'tom':tom})

# def CarstPage(request,id):
#     products = get_object_or_404(Products,id=id)
#     if request.method == 'POST':
#         user = request.user
#         Basket.objects.create(author=user,product=id)
#         return redirect('user:profile')
#     return render(request,'user/carts.html',{'product':products})


def LoginPage(request):
    if request.method == 'POST':
        if 'login_form' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('main:home')
        elif 'sign' in request.POST:
            username1 = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                if User.objects.filter(username=username1).exists():
                    return redirect('user:login')
                if User.objects.filter(email=email).exists():
                    return redirect('user:login')
                else:
                    user =User.objects.create_user(username=username1,password=password1,email=email)
                    user.save()
                    login(request,user)
                    return redirect('main:home')
            else:
                return redirect('user:login')
    return render(request,'user/loging.html')

def LogoutViews(request):
    logout(request)
    return redirect('main:home')