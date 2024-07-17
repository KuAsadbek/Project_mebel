from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,ListView,View
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from .models import Products,ProductPhoto

# def CommentViews(request,slug):
#     product = get_object_or_404(Products,slug=slug)
#     Tom = CommentMod.objects.filter(auothor=product)

#     if request.method == 'POST':
#         user = request.user
#         com = request.POST.get('comment','')
#         if com.strip():
#             CommentMod.objects.create(username=user,auothor=product,comment=com)
#         Tom = CommentMod.objects.filter(auothor=product)
#     return render(request,"product/product.html",{'posts':Tom,'product':product})



def SearchViews(request):
    query = None
    result = []
    if 'query' in request.GET:
        query = request.GET.get('query')
        result = Products.objects.filter(title__icontains=query)
    return render(request,'main/index.html',{'query':query,'products':result})

class DetailPage(DetailView):
    model = Products
    template_name = 'product/product.html'
    context_object_name = 'product'

class CategoryPage(View):
    def get(self,request, slug):

        products = Products.objects.filter(category__slug=slug)
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

            
        return render(request, 'product/catalog.html', {'products': page})


# class CategoryPage(ListView):
#     model = Products
#     template_name = 'product/catalog.html'
#     context_object_name = 'products'





# class CommentViews(View):
#     template_name = 'product/product.html'

#     def get(self, request, slug):
#         product = get_object_or_404(Products, slug=slug)
#         comments = CommentMod.objects.filter(author=product)
#         return render(request, self.template_name, {'posts': comments, 'product': product})

#     def post(self, request, slug):
#         product = get_object_or_404(Products, slug=slug)
#         user = request.user
#         comment_text = request.POST.get('comment', '')
#         if comment_text.strip():
#             CommentMod.objects.create(username=user, author=product, comment=comment_text)
#         comments = CommentMod.objects.filter(author=product)
#         return render(request, self.template_name, {'posts': comments, 'product': product})
