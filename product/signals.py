# product/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        message = {
            "message": f" Новый товар создан: {instance.title}"
        }
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": message,
            }
        )
