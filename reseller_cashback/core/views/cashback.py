import requests
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from requests.exceptions import RequestException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class CashBackReseller(APIView):  # type: ignore
    @swagger_auto_schema(  # type: ignore
        operation_description='cashback accumulated so far',
        responses={200: '{"credit":"0000"}'},
    )
    def get(self, request: Request, cpf_reseller: str) -> Response:
        try:
            resp = requests.get(
                settings.CASHBACK_API_TARGET,
                params={'cpf': cpf_reseller},
                headers={'token': settings.CASHBACK_API_TOKEN},
            )
            resp.raise_for_status()
        except RequestException as ex:
            return Response(str(ex), status=400)

        else:
            req = resp.json()

            if req['statusCode'] == 200:
                return Response(req['body'])
            else:
                return Response(req['body'], status=req['statusCode'])
