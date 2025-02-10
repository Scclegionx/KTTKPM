from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/books.html', context)
