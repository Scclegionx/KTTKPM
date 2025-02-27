from django.urls import path
from .views import shop, book_detail, clothes_detail, shoes_detail, electronics_detail

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('shop/book/<str:book_id>/', book_detail, name='book_detail'),
    path('shop/clothes/<str:clothes_id>/', clothes_detail, name='clothes_detail'),
    path('shop/shoes/<str:shoes_id>/', shoes_detail, name='shoes_detail'),
    path('shop/electronics/<str:electronics_id>/', electronics_detail, name='electronics_detail'),
]