# from django.shortcuts import render
# from book.models import Book

# def book_list_view(request):
#     books = Book.objects.all()
#     return render(request, 'book/book_list.html', {'books': books})

import requests
from django.shortcuts import render

def book_list_view(request):
    # JWT token lấy từ API /api/token/
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMzIwMTI3LCJpYXQiOjE3NDAzMTk4MjcsImp0aSI6Ijk0YjYzMTVjMzNjMDRiMDg5ZjI5MmZlNWZkYmM2OTdiIiwidXNlcl9pZCI6M30.dcfP_p_M1IzogInVQ-vaeTN4vHHmymDWvPHj8CJ3s5k" 

    # Thêm token vào header Authorization
    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }

    # Gọi API lấy danh sách book
    response = requests.get('http://127.0.0.1:8000/api/books/', headers=headers)
    
    # Chuyển JSON thành Python object
    books = response.json() if response.status_code == 200 else []

    # Ném data vào template
    return render(request, 'book/book_list.html', {'books': books})
