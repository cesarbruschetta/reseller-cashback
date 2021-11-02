from django.urls import include, path
from rest_framework_nested import routers

from .views import CashBackReseller, ResellerViewSet, SalesOrderViewSet


core_router = routers.SimpleRouter()
core_router.register(r'reseller', ResellerViewSet)
core_router.register(r'sales-order', SalesOrderViewSet)


urlpatterns = [
    path(
        '',
        include(core_router.urls),
    ),
    path(
        'cash-back/<cpf_reseller>/',
        CashBackReseller.as_view(),
        name='cash-back-reseller',
    ),
]
