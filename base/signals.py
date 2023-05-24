""" from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import SpecialRequest


@receiver(post_save, sender=SpecialRequest)
def revert_extension_requested(sender, instance, created, **kwargs):
    if created:
        borrowing = instance.product.borrowing_set.first()
        if borrowing:
            borrowing.extension_requested = not borrowing.extension_requested
            borrowing.save(update_fields=["extension_requested"]) """
