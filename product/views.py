from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Profile, Category, Tags, Product
from .serializers import UserSerializer, ProfileSerializer, CategorySerilalizer, TagsSerializer, ProductSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  

@method_decorator(csrf_exempt, name='dispatch')
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]  

@method_decorator(csrf_exempt, name='dispatch')
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilalizer
    permission_classes = [AllowAny]  

@method_decorator(csrf_exempt, name='dispatch')
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [AllowAny]  

@method_decorator(csrf_exempt, name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  



class ProductListView(ListView):
    model = Product
    template_name = 'index.html'  

class ProductDetailView(DetailView):
    model = Product
    template_name = 'index.html'  

def index(request):
    return render(request, 'index.html')