# from rest_framework.routers import DefaultRouter
# from .views import ElectronicsViewSet

# router = DefaultRouter()
# router.register(r'electronics', ElectronicsViewSet, basename='electronics')

# urlpatterns = router.urls

# electronics/urls.py
from django.urls import path
from .views import electronics_list, electronics_detail

urlpatterns = [
    path('electronics/', electronics_list, name='electronics-list'),
    path('electronics/<int:pk>/', electronics_detail, name='electronics-detail'),
]

