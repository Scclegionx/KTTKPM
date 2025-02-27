# seller/urls.py
from rest_framework.routers import DefaultRouter
from .views import SellerAuthViewSet

router = DefaultRouter()
router.register(r'auth', SellerAuthViewSet, basename='seller-auth')

urlpatterns = router.urls