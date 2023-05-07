import random
import string


def get_user_type(request):
    user = request.user
    if user.is_admin:
        return "admin"
    if user.is_mod:
        return "moderator"
    return "user"


def upload_to_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = f"{instance.name}_{instance.id}" if instance.name else str(instance.id)
    random_str = "".join(random.choice(string.ascii_lowercase) for _ in range (5))
    return f"images/{instance._meta.verbose_name_plural}/{filename}/{random_str}.{extension}"
