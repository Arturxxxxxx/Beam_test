from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Profile, Category, Tags

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerilalizer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'

