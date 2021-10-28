from typing import Any, List

from core.models import ResellerModel
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets

from ..serializers import ResellerSerializer


@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_description='Return all data of the Reseller',
    ),
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        operation_description='Update Reseller object',
    ),
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_description='Register new Reseller',
    ),
)
class ResellerViewSet(
    mixins.CreateModelMixin,  # type: ignore
    mixins.RetrieveModelMixin,  # type: ignore
    mixins.UpdateModelMixin,  # type: ignore
    viewsets.GenericViewSet,  # type: ignore
):
    queryset = ResellerModel.objects.all()
    serializer_class = ResellerSerializer
    permission_classes_by_action = {'create': [permissions.AllowAny]}

    def get_permissions(self) -> List[Any]:
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[
                    self.action
                ]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
