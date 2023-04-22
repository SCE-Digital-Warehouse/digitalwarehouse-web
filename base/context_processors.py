from django.conf import settings


def project_name(request):
    return {"PROJECT_NAME": settings.PROJECT_NAME}


def current_year(request):
    return {"CURRENT_YEAR": settings.CURRENT_YEAR}
