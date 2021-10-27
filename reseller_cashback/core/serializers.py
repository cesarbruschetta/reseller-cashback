from rest_framework import serializers

from .models import BaseModelMixin


class BaseSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = BaseModelMixin
        fields = '__all__'
