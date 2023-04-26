def get_user_type(request):
    user = request.user
    if user.is_admin:
        return "admin"
    if user.is_mod:
        return "moderator"
    return "user"
