from django.contrib import admin
from .models import Product, Category, Profile, Tags

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Tags)
