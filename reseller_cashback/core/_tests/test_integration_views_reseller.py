import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture()
def reseller_data(reseller_user):
    return reseller_user.__dict__


@pytest.fixture
def request_data():
    return {
        'full_name': 'Maria Jose',
        'password': '8DW06WAm',
        'email': 'maria.jose@reseller.io',
        'cpf': '85196580085',
    }


def test_should_register_new_reseller(db, client, request_data):
    response = client.post(
        reverse('core:resellermodel-list'),
        data=request_data,
    )
    assert response.status_code == 201
    register_reseller = response.data

    assert 'email' in register_reseller.keys()
    assert 'full_name' in register_reseller.keys()
    assert 'cpf' in register_reseller.keys()

    assert register_reseller['email'] == request_data['email']
    assert register_reseller['full_name'] == request_data['full_name']
    assert register_reseller['cpf'] == request_data['cpf']


def test_should_register_reseller_with_error(db, client, reseller_user):
    response = client.post(
        reverse('core:resellermodel-list'),
        data={'full_name': 'Silva', 'email': reseller_user.email},
    )
    assert response.status_code == 400
    register_reseller = response.data

    assert register_reseller['full_name'][0] == 'Please enter full name.'
    assert register_reseller['email'][0] == 'The e-mail must be unique.'


def test_should_update_profile_of_user(db, reseller_user, request_data):
    client = APIClient()
    client.force_authenticate(user=reseller_user)

    response = client.put(
        reverse('core:resellermodel-detail', args=(reseller_user.pk,)),
        data=request_data,
    )
    assert response.status_code == 200

    about_me_user = response.data
    for key, value in request_data.items():
        if key not in ['full_name', 'password', 'email', 'cpf']:
            assert about_me_user[key] == value
