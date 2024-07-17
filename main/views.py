from django.shortcuts import render,redirect
# from django.urls import reverse_lazy
from django.views.generic import DeleteView,CreateView,UpdateView,DetailView,View,ListView
from product.models import Products
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def MainPage(request):
    return render(request,'main/main_.html')


class HomePage(View):
    def get(self,request):
        products = Products.objects.all()
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            # Если page_number не является целым числом, устанавливаем значение на первую страницу
            page = paginator.page(1)
        except EmptyPage:
            # Если page_number больше, чем общее количество страниц, устанавливаем значение на последнюю страницу
            page = paginator.page(paginator.num_pages)
        return render(request,'main/index.html',{'products':page})


def AboutUs(request):
    return render(request,'main/about.html')


# def PaginatorPage(request):
#     if slug == 'all':
#             products = Products.objects.all()
#             paginator = Paginator(products, 1)
#     else:
#         products = Products.objects.filter(category__slug=slug)
#         paginator = Paginator(products, 2)

#     page_number = request.GET.get('page')
    
#     try:
#         page = paginator.page(page_number)
#     except PageNotAnInteger:
#         # Если page_number не является целым числом, устанавливаем значение на первую страницу
#         page = paginator.page(1)
#     except EmptyPage:
#         # Если page_number больше, чем общее количество страниц, устанавливаем значение на последнюю страницу
#         page = paginator.page(paginator.num_pages)
#     return render(request,'main/nav.html',{'page_obj':page_obj})




# def HomePage(request):
#     products = Products.objects.all()
#     return render(request,'main/index.html',{'products':products})


# # ListView это чтоб вывести данные на сайт
# class StorePage(ListView):
#     model = Products
#     template_name = 'main/index.html'
#     context_object_name = 'products'

# CreateView это для добавление товара
# class CreateViews(CreateView):
#     model = Main_table
#     form_class = ProductForm
#     template_name = 'main/create.html'
#     success_url = reverse_lazy('home')

# # UpdateView ну ты сам знаешь
# class UpdatePage(UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name='main/update.html'
#     success_url = reverse_lazy('home')


# # DeleteView эта тоже
# class DeletePage(DeleteView):
#     model = Product
#     template_name='main/delete.html'
#     success_url = reverse_lazy('home')


