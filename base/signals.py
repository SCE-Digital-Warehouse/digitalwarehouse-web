from django.dispatch import receiver
from django.db.models.signals import pre_delete

from .models import User, Request, Borrowing, Repair


@receiver(pre_delete, sender=User)
def user_pre_delete_handler(sender, instance, **kwargs):
    try:
        requests = Request.objects.filter(user=instance)
        for request in requests:
            request.product.change_availability()
    except Exception:
        try:
            borrowings = Borrowing.objects.filter(user=instance)
            for borrowing in borrowings:
                borrowing.product.change_availability()
        except Exception:
            try:
                repairs = Repair.objects.filter(user=instance)
                for repair in repairs:
                    repair.product.change_availability()
            except Exception:
                pass
