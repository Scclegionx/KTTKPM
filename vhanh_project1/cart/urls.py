from django.urls import path
from cart import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<str:product_id>/<str:product_name>/<str:price>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
]
