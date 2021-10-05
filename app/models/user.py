from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    ROLE = (
        ('main', 'Main'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=10, choices=ROLE, null=True, blank=True)

    class Meta:
        app_label = "app"
