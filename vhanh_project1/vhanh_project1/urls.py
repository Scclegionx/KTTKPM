from django.contrib import admin
from django.urls import path, include
from .views import home
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('', include('customer.urls')),
    path('', include('cart.urls')),
    path('home/', home, name='home'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
