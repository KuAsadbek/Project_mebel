from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # path('product<slug:slug>/',views.,name='detail'),
    path('product<slug:slug>/',views.DetailPage.as_view(),name='detail'),
    path('catalog/<slug:slug>/',views.CategoryPage.as_view(),name='category'),
    path('search/',views.SearchViews,name='search'),
]
