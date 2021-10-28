import pytest
from model_bakery import baker


@pytest.fixture
def reseller_user(db):
    reseller = baker.make(
        'core.ResellerModel',
        cpf='89011577051',
        email='user_1@reseller.io',
    )
    reseller.set_password('abc123456')
    return reseller


@pytest.fixture
def sales_order(db):
    return baker.make(
        'core.SalesOrderModel',
        cpf_reseller='89011577051',
        value=100.00,
    )
