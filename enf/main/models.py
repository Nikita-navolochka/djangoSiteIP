from django.db import models
from  django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
# class Grade(models.Models): #
#     name = models.CharField(max_length=10)


#     def __str__(self):
#         return self.name
    
class Product(models.Model):
     name = models.CharField(max_length=100)
     slug = models.CharField(max_length=100, unique=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                  related_name='products')
     subject = models.CharField(max_length=100)
     author = models.CharField(max_length=200)
     description = models.TextField(blank=True)
     link = models.CharField(max_length=300)
     main_image = models.ImageField(upload_to='products/main/')
     grade = models.CharField(max_length=3)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     part = models.CharField(max_length=5, blank=True)

     def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
     def __str__(self):
        return self.name
     
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='products/extra/')