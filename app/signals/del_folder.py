from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from app.models.product import Product


# @receiver(pre_delete, sender=Product)
# def photo_post_delete_handler(sender, **kwargs):
#     photo = kwargs['instance']
#     storage, path = photo.image.storage, photo.image.path
#     storage.delete(path)
