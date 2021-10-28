'''reseller_cashback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
'''

from core.views import schema_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns_api_v1 = [
    path(
        'auth/', include(('authentication.urls', 'auth'), namespace='auth_jwt')
    ),
    path(
        'core/',
        include(('core.urls', 'core'), namespace='core'),
    ),
]

urlpatterns_swagger = [
    path('', RedirectView.as_view(url='/doc/swagger/'), name='doc-index'),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doc/', include(urlpatterns_swagger)),
    path('api/v1/', include(urlpatterns_api_v1)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler500 = 'rest_framework.exceptions.server_error'
