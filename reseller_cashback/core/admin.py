from typing import Any, Tuple

from django.contrib import admin


def _set_defaults_values_fields(
    obj: Any, defaults_fields: Tuple[Tuple[str, Tuple[str, ...]], ...]
) -> None:
    for field, default_value in defaults_fields:
        setattr(obj, field, getattr(obj, field, ()) + default_value)


class BaseAdmin(admin.AdminSite):  # type: ignore
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults_fields = (
            ('list_display', ('id', 'created_at', 'updated_at')),
            ('list_filter', ('updated_at',)),
            ('search_fields', ('id',)),
            (
                'readonly_fields',
                ('created_at', 'created_by'),
            ),
        )

        super().__init__(*args, **kwargs)
        _set_defaults_values_fields(self, defaults_fields)
