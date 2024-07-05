# In myapp/urls.py

from django.urls import path
from .views import RegisterAPIView, LoginAPIView
from .import views

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('reviews/', views.ReviewCreate.as_view(), name='review-create'),
]
