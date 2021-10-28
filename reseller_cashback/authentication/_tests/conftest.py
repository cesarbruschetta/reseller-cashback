import pytest
from django.urls import reverse


@pytest.fixture
def payload_user(admin_user):
    return {
        'username': admin_user.username,
        'password': 'password',
    }


@pytest.fixture
def request_auth_create_token(client, payload_user):

    response = client.post(reverse('auth_jwt:create-token'), payload_user)
    assert response.status_code == 200

    return response.json()


@pytest.fixture()
def access_token(request_auth_create_token):
    return request_auth_create_token['access_token']
