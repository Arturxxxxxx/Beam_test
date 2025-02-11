from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.username

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name='Категория')

    def __str__(self):
        return self.category

class Tags(models.Model):
    tags = models.CharField(max_length=50, verbose_name='теги')

    def __str__(self):
        return self.tags

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(Tags, related_name='products', blank=True)
    title = models.CharField(max_length=100, verbose_name='название продукта')
    price = models.PositiveBigIntegerField(verbose_name='цена')
    description = models.CharField(max_length=500, verbose_name='описание')

    def __str__(self):
        return self.title
    

