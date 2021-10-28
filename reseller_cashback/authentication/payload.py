from typing import Any, Dict

from rest_framework_jwt.settings import api_settings


def jwt_response_payload_handler(
    token: str, user: Any = None, request: Any = None
) -> Dict[str, Any]:

    return {
        'access_token': token,
        'expires_in': api_settings.JWT_EXPIRATION_DELTA,
        'refresh_expires_in': api_settings.JWT_REFRESH_EXPIRATION_DELTA,
        'user_pk': user.pk,
    }
