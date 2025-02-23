from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book/', include('book.urls')),
    path('api/customer/', include('customer.urls')),
    path('', home, name='home'),
]
