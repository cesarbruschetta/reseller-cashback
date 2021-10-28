from django.urls import reverse


def test_should_login_in_system_oauth2_token(request_auth_create_token):
    create_token = request_auth_create_token

    assert 'access_token' in create_token.keys()
    assert 'expires_in' in create_token.keys()
    assert 'refresh_expires_in' in create_token.keys()


def test_should_refresh_token(client, access_token):

    response = client.post(
        reverse('auth_jwt:refresh-token'), {'token': access_token}
    ).json()

    assert 'access_token' in response.keys()
    assert 'expires_in' in response.keys()
    assert 'refresh_expires_in' in response.keys()
