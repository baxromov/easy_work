from django.db import models
from app.models.product import Product
from app.mixin.created_at import CreatedAtMixin


class History(models.Model, CreatedAtMixin):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    class Meta:
        app_label = "app"
