from .views import ProductListView, ProductDetailView, index
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, CategoryViewSet, TagViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
    path('product/', ProductListView.as_view(), name='product-list'),  
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  

]
