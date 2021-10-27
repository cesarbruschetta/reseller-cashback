from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .utils import get_domain


api_info = openapi.Info(
    title='CashBack Revendedor API',
    default_version='v1',
    description='',
    contact=openapi.Contact(
        name='reselercashback.com',
        url='https://www.reselercashback.com/',
        email='contato@reselercashback.com',
    ),
    license=openapi.License(
        name='MIT License',
        url='https://opensource.org/licenses/MIT',
    ),
)


schema_view = get_schema_view(
    api_info,
    url=f'{get_domain()}/api/v1',
    public=True,
    permission_classes=(permissions.AllowAny,),
)
