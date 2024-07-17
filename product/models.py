from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=150,unique=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    # def get_absolute_url(self):
    #      return reverse('category_post',args=[self.slug])
    

class Products(models.Model):
    category  = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True,null=True,blank=True)
    count = models.IntegerField()
    price = models.BigIntegerField()
    description = models.TextField()
    skid = models.IntegerField(null=True,blank=True)

    # class Meta:
    #      ordering = (id,)

    def __str__(self) -> str:
            return self.title
    
    # def get_absolute_url(self):
    #      return reverse('',args=[self.slug])
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.skid:
            return round(self.price * (1-self.skid/100))
        return self.price

class ProductPhoto(models.Model):
    product = models.ForeignKey(to=Products,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photo')

# class CommentMod(models.Model):
#      username = models.CharField(max_length=50)
#      comment = models.TextField()
#      auothor = models.CharField(max_length=70)



