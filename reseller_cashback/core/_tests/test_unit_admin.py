from core.admin import SalesOrderAdmin
from core.models import SalesOrderModel
from django.contrib.admin.sites import AdminSite


def test_should_cashback_for_admin(sales_order):
    admin = SalesOrderAdmin(model=SalesOrderModel, admin_site=AdminSite())
    value = admin.cashback(sales_order)
    assert isinstance(value, float)
    assert value == 10.0
