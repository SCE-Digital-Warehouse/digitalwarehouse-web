import random
import string
from urllib.parse import urlparse


def get_user_type(request):
    user = request.user
    if user.is_admin:
        return "admin"
    if user.is_mod:
        return "moderator"
    return "user"


def upload_to_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = f"{instance.name}_{instance.id}" if instance.name else str(
        instance.id)
    random_str = "".join(random.choice(string.ascii_lowercase)
                         for _ in range(5))
    return f"images/{instance._meta.verbose_name_plural}/{filename}/{random_str}.{extension}"


def get_previous_template(referer):
    if referer:
        parsed_url = urlparse(referer)
        path_segments = parsed_url.path.strip('/').split('/')
        template_name = path_segments[0] if path_segments else None
    return template_name
