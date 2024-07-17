from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class User_register(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')













# class MainTableForm(forms.ModelForm):
#     class Meta:
#         model = Main_table
#         fields = ('name', 'slug')
#         labels = {
#             'name': 'Название',
#             'slug': 'Slug',
#         }
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'slug': forms.TextInput(attrs={'class': 'form-control'}),
#         }

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'slug', 'descriptions', 'photo', 'price', 'discount', 'quantity', 'category')
#         labels = {
#             'name': 'Название',
#             'slug': 'Slug',
#             'descriptions': 'Описание',
#             'photo': 'Фото',
#             'price': 'Цена',
#             'discount': 'Скидка',
#             'quantity': 'Количество',
#             'category': 'Категория',
#         }
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'slug': forms.TextInput(attrs={'class': 'form-control'}),
#             'descriptions': forms.Textarea(attrs={'class': 'form-control'}),
#             'photo': forms.FileInput(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'discount': forms.NumberInput(attrs={'class': 'form-control'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#         }


