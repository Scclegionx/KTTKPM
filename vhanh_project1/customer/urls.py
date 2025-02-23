from django.urls import path
from .views import profile, login_page, logout_user, register_page

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_user, name='logout'),
]
