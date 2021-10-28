from typing import Any

from core.models import BaseModel
from django.db import models
from localflavor.br.models import BRCPFField


class SalesOrderModel(BaseModel):
    class Meta(BaseModel.Meta):
        verbose_name = 'Sales Order'
        verbose_name_plural = 'Sales Orders'
        ordering = [
            '-created_at',
        ]

    class StatusChoice(models.TextChoices):  # type: ignore
        IN_VALIDATION = 'in_validation', 'In validation'
        APPROVED = 'approved', 'Approved'

    code = models.CharField(max_length=256, verbose_name='Code')
    value = models.DecimalField(
        decimal_places=2,
        max_digits=20,
        default=0.0,
        verbose_name='Total value',
    )
    cpf_reseller = BRCPFField(verbose_name='CPF')
    status = models.CharField(
        max_length=20,
        choices=StatusChoice.choices,
        default=StatusChoice.IN_VALIDATION,
        verbose_name='Status',
    )

    def get_cashback(self) -> Any:
        if 0.0 < self.value <= 1000.0:
            return self.value * 0.10
        elif 1000.0 < self.value <= 1500.0:
            return self.value * 0.15
        elif self.value > 1500.0:
            return self.value * 0.20
        else:
            return 0.0
