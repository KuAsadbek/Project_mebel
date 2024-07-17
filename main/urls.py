from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('Index',views.HomePage.as_view(),name='home'),
    path('about',views.AboutUs,name='about'),
    path('',views.MainPage,name='main_page'),
    # path('sign',login_signup,name='sing'),
    # path("logout", LogoutViews,  name = "logout"),
    # path('store',StorePage.as_view(),name='store'),
    # path('create',CreateViews.as_view(),name='create'),
    # path('u:pdate/<int:pk>',UpdatePage.as_view(),name='update'),
    # path('delete/<intpk>',DeletePage.as_view(),name='delete'),
    # path('detail/<int:pk>',DetailPage.as_view(),name='detail'),
]
