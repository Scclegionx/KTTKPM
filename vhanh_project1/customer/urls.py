from django.urls import path
from customer import views

urlpatterns = [
    path('login/', views.customer_login, name='login'),
    path('register/', views.customer_register, name='register'),
    # path('profile/', views.profile, name='profile'),
    path('logout/', views.customer_logout, name='logout'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
