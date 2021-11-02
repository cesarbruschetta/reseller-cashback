import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture()
def sales_order_data(sales_order):
    return sales_order.__dict__


@pytest.fixture()
def client(reseller_user):
    client = APIClient()
    client.force_authenticate(user=reseller_user)
    return client


def test_should_create_salesorder(db, client, sales_order_data):
    sales_order_data['cpf_reseller'] = '15350946056'

    response = client.post(
        reverse('core:salesordermodel-list'),
        data=sales_order_data,
    )
    assert response.status_code == 201
    req = response.data

    assert 'status' in req.keys()
    assert req['status'] == 'approved'


def test_should_update_salesorder_approved(
    db, client, sales_order, sales_order_data
):
    sales_order.status = 'approved'
    sales_order.save()

    response = client.put(
        reverse('core:salesordermodel-detail', args=(sales_order.pk,)),
        data=sales_order_data,
    )
    assert response.status_code == 400
    req = response.data
    assert (
        req['non_field_errors'][0] == 'Sale order approved disallow editing.'
    )


def test_should_destroy_salesorder_approved(db, client, sales_order):
    sales_order.status = 'approved'
    sales_order.save()

    response = client.delete(
        reverse('core:salesordermodel-detail', args=(sales_order.pk,)),
    )
    assert response.status_code == 400
    req = response.data
    assert req['message'] == 'Sale order approved disallow to delete'


def test_should_destroy_salesorder(db, client, sales_order):
    response = client.delete(
        reverse('core:salesordermodel-detail', args=(sales_order.pk,)),
    )
    assert response.status_code == 204
