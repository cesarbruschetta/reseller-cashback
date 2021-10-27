from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from .views import obtain_jwt_token


urlpatterns = [
    path('token/', obtain_jwt_token, name='create-token'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token'),
]
