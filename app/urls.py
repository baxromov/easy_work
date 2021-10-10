from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from app import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('product', views.ProductTemplateView.as_view(), name='product'),
    path('product_json', views.product_json, name='product_json'),
    path("logout", LogoutView.as_view(), name="logout"),
    path("login", LoginView.as_view(template_name='app/authentication/login.html', redirect_field_name='home'), name="login"),
    path("registration", views.Registration.as_view(), name="registration"),
]
