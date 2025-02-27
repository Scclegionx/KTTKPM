from django.contrib import admin
from django.urls import path, include
from .views import home
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
    path('api/', include('book.urls')),
    path('', include('customer.urls')),
    path('api/seller/', include('seller.urls')),
    path('', include('cart.urls')),
    path('api/', include('clothes.urls')),
    path('', include('base.urls')),
    path('home/', home, name='home'),
    path('api/', include('shoes.urls')),
    path('api/', include('electronics.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('coupons.urls')),
    # path('', include('payment.urls')),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
