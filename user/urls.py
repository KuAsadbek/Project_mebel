from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
   # path('Profile/',views.ProfilePage,name='profile'),
   # path('Carts/<int:id>/',views.CarstPage,name='Carts'),
   path('login',views.LoginPage,name='login'),
   path('logout',views.LogoutViews,name='logout'),
]
