from django.urls import path
from book import api, views

urlpatterns = [
    # API endpoints
    path('api/books/', api.book_list),
    path('api/books/<book_id>/', api.book_detail),

    # MVT views
    path('books/', views.book_list_view),
]
