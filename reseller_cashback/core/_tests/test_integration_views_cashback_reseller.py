from core.views import cashback
from django.urls import reverse
from requests.exceptions import ConnectionError
from rest_framework.test import APIClient


def test_should_amout_of_cashback(reseller_user, mocker):
    fake_requests = mocker.patch.object(cashback, 'requests')
    fake_requests.get.return_value.json.return_value = {
        'statusCode': 200,
        'body': {'credit': 1803},
    }

    client = APIClient()
    client.force_authenticate(user=reseller_user)
    response = client.get(
        reverse('core:cash-back-reseller', args=('37474173883',)),
    )
    assert response.status_code == 200
    data = response.data

    assert 'credit' in data.keys()
    assert data['credit'] == 1803


def test_should_amout_of_cashback_badrequest(reseller_user, mocker):
    fake_requests = mocker.patch.object(cashback, 'requests')
    fake_requests.get.return_value.json.return_value = {
        'statusCode': 400,
        'body': {
            'message': 'CPF do revendedor(a) está incorreto, utilize apenas números!'
        },
    }

    client = APIClient()
    client.force_authenticate(user=reseller_user)
    response = client.get(
        reverse('core:cash-back-reseller', args=('37474173883',)),
    )
    assert response.status_code == 400
    data = response.data

    assert 'message' in data.keys()
    assert (
        data['message']
        == 'CPF do revendedor(a) está incorreto, utilize apenas números!'
    )


def test_should_amout_of_cashback_with_error(reseller_user, mocker):
    fake_requests = mocker.patch.object(cashback, 'requests')
    fake_requests.get.side_effect = ConnectionError('fake error')

    client = APIClient()
    client.force_authenticate(user=reseller_user)
    response = client.get(
        reverse('core:cash-back-reseller', args=('37474173883',)),
    )
    assert response.status_code == 400
