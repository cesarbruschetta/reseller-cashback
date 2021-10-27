from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken


User = get_user_model()


class CustomObtainJSONWebToken(ObtainJSONWebToken):  # type: ignore
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super(CustomObtainJSONWebToken, self).post(
            request, *args, **kwargs
        )
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(pk=response.data['user_pk'])
            user_logged_in.send(
                sender=user.__class__, request=request, user=user
            )

        return response


obtain_jwt_token = CustomObtainJSONWebToken.as_view()
