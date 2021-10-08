from django.db import models

from app.mixin import created_at
from app.models.category import Category


def get_directory(instance, filename):
    return 'product/{0}/{1}'.format(instance.category.name, filename)


class Product(created_at.CreatedAtMixin, models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    measurement = models.CharField(max_length=20, default='шт', null=True, blank=True)

    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to=get_directory, null=True, blank=True)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path

        super(Product, self).delete(*args, **kwargs)
        storage.delete(path)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "app"
