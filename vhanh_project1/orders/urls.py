from django.urls import path
from orders import views

# seller/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')


urlpatterns = [
    path('order/preview/', views.order_preview, name='order_preview'),
    path('order/confirm/', views.confirm_order, name='confirm_order'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),
] + router.urls
