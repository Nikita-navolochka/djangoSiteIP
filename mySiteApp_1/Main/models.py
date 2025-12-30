from django.db import models
from  django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)


    def save(self, *args, **kwargs):
        # Если slug пустой — генерируем уникальный slug на основе name
        if not self.slug:
            base = slugify(self.name)[:90]  # оставим запас для суффикса
            slug = base
            i = 1
            # убеждаемся, что slug уникален
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        # ВСЕГДА вызываем родительский save, чтобы объект действительно сохранился
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
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=300)
    main_image = models.ImageField(upload_to='products/main/')
    grade = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    part = models.CharField(max_length=5, blank=True)

    def save(self, *args, **kwargs):
        # Генерируем slug, если он пустой, и обеспечиваем уникальность
        if not self.slug:
            base = slugify(self.name)[:90]
            slug = base
            i = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        # ВСЕГДА сохраняем объект
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
     
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='products/extra/')