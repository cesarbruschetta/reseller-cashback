import uuid
from typing import Any

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):  # type: ignore

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at'
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self) -> str:
        title = getattr(self, 'title', self.id)
        return f'{self._meta.verbose_name}: {title}'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
