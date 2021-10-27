from django.conf import settings
from django.contrib.sites.models import Site


def get_domain() -> str:
    try:
        site = Site.objects.get_current()
    except Exception:
        return ''
    else:
        return f'{settings.HOST_PROTOCOL}://{site.domain}'
