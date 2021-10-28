from core.serializers import SalesOrderSerializer


def test_should_serializer_user_raise_email(sales_order):
    serializer = SalesOrderSerializer(instance=sales_order)

    data = serializer.data
    keys = [
        'code',
        'cpf_reseller',
        'status',
    ]
    for key in keys:
        assert key in data.keys()
        assert data[key] == getattr(sales_order, key)

    assert 'value' in data.keys()
    assert 'cashback' in data.keys()
    assert 'date' in data.keys()

    assert float(data['value']) == sales_order.value
    assert data['cashback'] == sales_order.get_cashback()
    assert data['date'] == sales_order.created_at.date()
