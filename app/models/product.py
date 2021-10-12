from django.db import models

from app.mixin import created_at
from app.models import user
from app.models.category import Category


def get_directory(instance, filename):
    return 'product/{0}/{1}'.format(instance.category.name, filename)


class Product(created_at.CreatedAtMixin, models.Model):
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Наименование")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Категория")
    measurement = models.CharField(max_length=20, default='шт', null=True, blank=True, verbose_name="Измерение")

    price = models.FloatField(default=0, verbose_name="Цена (Сум)")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    image = models.ImageField(upload_to=get_directory, null=True, blank=True, verbose_name="Изображение")

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path

        super(Product, self).delete(*args, **kwargs)
        storage.delete(path)

    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = "app"
        verbose_name_plural = "Товары"
