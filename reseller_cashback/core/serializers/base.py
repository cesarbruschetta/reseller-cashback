from rest_framework import serializers

from ..models import BaseModel


class BaseSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = BaseModel
        fields = '__all__'
