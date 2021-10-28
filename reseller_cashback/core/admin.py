from typing import Any, Tuple

from core.models import ResellerModel, SalesOrderModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


def _set_defaults_values_fields(
    obj: Any, defaults_fields: Tuple[Tuple[str, Tuple[str, ...]], ...]
) -> None:
    for field, default_value in defaults_fields:
        setattr(obj, field, getattr(obj, field, ()) + default_value)


class BaseAdmin(admin.ModelAdmin):  # type: ignore
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults_fields = (
            ('list_display', ('id', 'created_at', 'updated_at')),
            ('list_filter', ('updated_at',)),
            ('search_fields', ('id',)),
            ('readonly_fields', ('created_at', 'updated_at')),
        )

        super(BaseAdmin, self).__init__(*args, **kwargs)
        _set_defaults_values_fields(self, defaults_fields)


class ResellerAdmin(UserAdmin):  # type: ignore
    search_fields = ('username', 'email')


class SalesOrderAdmin(BaseAdmin):
    list_display = ('code', 'status', 'value', 'cashback')

    def cashback(self, obj: SalesOrderModel) -> Any:
        return obj.get_cashback()


admin.site.register(ResellerModel, ResellerAdmin)
admin.site.register(SalesOrderModel, SalesOrderAdmin)
