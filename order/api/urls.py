from order.api.views import OrderV, OrderDetailV
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('list', OrderV, basename='order-list')
router.register('list-detail', OrderDetailV, basename='order-detail')

urlpatterns = [
    path('', include(router.urls))
]

