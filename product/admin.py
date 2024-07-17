from django.contrib import admin
from .models import Category,Products,ProductPhoto



# class AdminProduct(admin.ModelAdmin):
#     list_display = ['author','title','price',]

class CategorySlug(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ImageProduct(admin.TabularInline):
    model = ProductPhoto

class YourModelAdmin(admin.ModelAdmin):
    inlines = [ImageProduct]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Products, YourModelAdmin)

admin.site.register(Category,CategorySlug)

# Register your models here.
