from django.db import models












# class Main_table(models.Model):
#     name = models.CharField(max_length=150,unique=True,verbose_name='Названые!')
#     slug = models.SlugField(max_length=200,unique=True,blank=True,null=True,verbose_name='Slug!')

#     class Meta:
#         verbose_name_plural='Категории'

#     def __str__(self) -> str:
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=150,unique=True)
#     slug = models.CharField(max_length=200,unique=True,blank=True,null=True)
#     descriptions = models.TextField(blank=True,null=True)
#     photo = models.ImageField(upload_to=True,blank=True,null=True)
#     price = models.DecimalField(default=0.00,max_digits=7,decimal_places=2)
#     discount = models.DecimalField(default=0.00,max_digits=4,decimal_places=2)
#     quantity = models.PositiveIntegerField(default=0)
#     category = models.ForeignKey(to=Main_table,on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f'{self.name} - количество:{self.quantity}'
