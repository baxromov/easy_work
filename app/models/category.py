from django.db import models

from app.mixin import created_at
from app.models import user


class Category(models.Model, created_at.CreatedAtMixin):
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "app"
