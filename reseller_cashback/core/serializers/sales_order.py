from typing import Any, Dict

from core.serializers import BaseSerializer
from rest_framework import serializers

from ..models import SalesOrderModel


class SalesOrderSerializer(BaseSerializer):  # type: ignore
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

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if (
            self.instance
            and self.instance.status
            == SalesOrderModel.StatusChoice.APPROVED.value  # type: ignore
        ):
            raise serializers.ValidationError(
                "Sale order approved disallow editing."
            )

        if (
            data['cpf_reseller'].replace('.', '').replace('-', '')
            == '15350946056'
        ):
            data['status'] = SalesOrderModel.StatusChoice.APPROVED.value  # type: ignore

        return data
