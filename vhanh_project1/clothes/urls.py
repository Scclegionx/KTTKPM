# from django.urls import path
# from . import views

# urlpatterns = [
#     path('api/clothes/', views.clothes_list, name='clothes_list'),
#     path('api/clothes/<str:pk>/', views.clothes_detail, name='clothes_detail'),
# ]

# clothes/urls.py
from rest_framework.routers import DefaultRouter
from .views import ClothesViewSet

router = DefaultRouter()
router.register(r'clothes', ClothesViewSet, basename='clothes')

urlpatterns = router.urls
