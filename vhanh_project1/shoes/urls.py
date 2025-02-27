from rest_framework.routers import DefaultRouter
from .views import ShoesViewSet

router = DefaultRouter()
router.register(r'shoes', ShoesViewSet, basename='shoes')

urlpatterns = router.urls