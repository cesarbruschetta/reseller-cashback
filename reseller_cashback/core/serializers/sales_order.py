from typing import Any

from core.serializers import BaseSerializer
from rest_framework import serializers

from ..models import SalesOrderModel


class SalesOrderSerializer(BaseSerializer):
    date = serializers.SerializerMethodField()
    cashback = serializers.SerializerMethodField()

    class Meta:
        model = SalesOrderModel
        exclude = (
            'created_at',
            'updated_at',
        )

    def get_date(self, obj: SalesOrderModel) -> Any:
        return obj.created_at.date()

    def get_cashback(self, obj: SalesOrderModel) -> Any:
        return obj.get_cashback()
