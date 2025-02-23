from django.urls import path
from cart import api, views

urlpatterns = [
    # API endpoints
    path('api/carts/', api.cart_list),
    path('api/carts/<cart_id>/', api.cart_detail),

    # MVT views
    path('carts/', views.cart_list_view),
]
