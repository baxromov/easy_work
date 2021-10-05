from django.contrib import admin
from app.models.user import User
from app.models.category import Category
from app.models.history import History
from app.models.product import Product


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(History)
class HistoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass


