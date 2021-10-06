from django.urls import path

from app import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('product', views.ProductTemplateView.as_view(), name='product'),
]
