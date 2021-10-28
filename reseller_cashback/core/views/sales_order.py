from core.models import SalesOrderModel
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from ..serializers import SalesOrderSerializer


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_description='List all Sales Order',
    ),
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Return data of the Sales Order',
    ),
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Register new Sales Order',
    ),
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_description='Update Sales Order object',
    ),
)
@method_decorator(
    name='destroy',
    decorator=swagger_auto_schema(
        operation_description='Remove Sales Order object',
    ),
)
class SalesOrderViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = SalesOrderModel.objects.all()
    serializer_class = SalesOrderSerializer
