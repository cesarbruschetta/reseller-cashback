import uuid
from typing import Any

from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRCPFField


class ResellerModel(AbstractUser):  # type: ignore
    '''Reseller model'''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    cpf = BRCPFField(verbose_name='CPF')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(AbstractUser.Meta):  # type: ignore
        verbose_name = 'Reseller'
        verbose_name_plural = 'Resellers'

    @property
    def full_name(self) -> str:
        name = f'{self.first_name} {self.last_name}'
        return name.strip() and name or str(self.pk)

    def save(self, *args: Any, **kwargs: Any) -> Any:
        self.first_name: str = self.first_name.title()
        self.last_name: str = self.last_name.title()

        return super(ResellerModel, self).save(*args, **kwargs)
