import pytest


def test_should__str__to_object(sales_order):
    assert 'Sales Order' in str(sales_order)


@pytest.mark.parametrize(
    'value,expected',
    [
        (100.0, 10.0),
        (1100.0, 165.0),
        (1700.0, 340.0),
        (0.0, 0.0),
    ],
)
def test_should_calculator_cashback_of_sales_order(
    sales_order, value, expected
):
    sales_order.value = value
    sales_order.save()

    assert sales_order.get_cashback() == expected
