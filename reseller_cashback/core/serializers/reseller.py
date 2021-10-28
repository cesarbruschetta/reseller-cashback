from typing import Any, Dict

from rest_framework import serializers

from ..models import ResellerModel
from .base import BaseSerializer


class ResellerSerializer(BaseSerializer):
    full_name = serializers.CharField(
        max_length=60,
        label="Full name",
    )

    class Meta(BaseSerializer.Meta):
        model = ResellerModel
        fields = ['full_name', 'email', 'cpf', 'password']  # type: ignore
        extra_kwargs = {'email': {'required': True}}

    def _parse_validated_data(
        self, validated_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        instance = self.instance
        name = validated_data.pop(
            'full_name', getattr(instance, 'full_name', ' ')
        )
        first_name, last_name = name.split(' ', 1)
        validated_data.update(
            {
                'first_name': first_name,
                'last_name': last_name,
                'username': validated_data.get(
                    'email', getattr(instance, 'email', '')
                ),
            }
        )
        return validated_data

    def validate_full_name(self, value: str) -> str:
        if not len(value.split()) > 1:
            # check name has more than 1 word
            raise serializers.ValidationError('Please enter full name.')
        return value

    def validate_email(self, value: str) -> str:
        # Determine the existing instance, if this is an update operation.
        instance = self.instance
        queryset = self.Meta.model.objects.filter(email=value)
        if instance is not None:
            queryset = queryset.exclude(pk=instance.pk)

        if queryset.exists():
            raise serializers.ValidationError('The e-mail must be unique.')
        return value

    def create(self, validated_data: Dict[str, Any]) -> Any:
        validated_data = self._parse_validated_data(validated_data)
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(
        self, instanse: ResellerModel, validated_data: Dict[str, Any]
    ) -> Any:
        validated_data = self._parse_validated_data(validated_data)
        validated_data.pop('username', None)
        return super().update(instanse, validated_data)
