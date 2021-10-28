from rest_framework_jwt.settings import api_settings


def test_should_response_response_payload_to_jwt(admin_user):

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

    payload = jwt_response_payload_handler(
        token=jwt_encode_handler(jwt_payload_handler(admin_user)),
        user=admin_user,
    )

    assert 'access_token' in payload.keys()
    assert 'expires_in' in payload.keys()
    assert 'refresh_expires_in' in payload.keys()
    assert 'user_pk' in payload.keys()
