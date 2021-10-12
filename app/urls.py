from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from app import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('category', views.CategoryListView.as_view(), name='category'),
    path('category/create', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('product', views.ProductTemplateView.as_view(), name='product'),
    path('product/create', views.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path("logout", LogoutView.as_view(), name="logout"),
    path("login", LoginView.as_view(template_name='app/authentication/login.html', redirect_field_name='home'), name="login"),
    path("registration", views.Registration.as_view(), name="registration"),
]
