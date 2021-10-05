from django.db import models


class CreatedAtMixin(object):
    created_at = models.DateTimeField(auto_now_add=True)
