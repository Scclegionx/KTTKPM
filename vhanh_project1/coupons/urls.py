from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CouponViewSet

router = DefaultRouter()
router.register(r'coupons', CouponViewSet, basename='coupon')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

urlpatterns = router.urls

