from django.db import models
from app.mixin import created_at


class Category(models.Model, created_at.CreatedAtMixin):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "app"
