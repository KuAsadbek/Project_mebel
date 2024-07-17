from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# class CastumerUser(AbstractUser):
#     title = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=80)
#     user = models.CharField(max_length=50)
#     email = models.EmailField()

#     def __str__(self) -> str:
#         return self.user

# class Basket(models.Model):
#     product = models.IntegerField()
#     author = models.ForeignKey('user.CastumerUser', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'buy product {self.product}' 
    