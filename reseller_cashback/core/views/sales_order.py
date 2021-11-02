from typing import Any

from core.models import SalesOrderModel
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

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
class SalesOrderViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = SalesOrderModel.objects.all()
    serializer_class = SalesOrderSerializer

    @swagger_auto_schema(  # type: ignore
        operation_description='Remove Sales Order object',
    )
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        obj = self.get_object()
        if obj.status == SalesOrderModel.StatusChoice.APPROVED.value:
            return Response(
                data={'message': "Sale order approved disallow to delete"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)
