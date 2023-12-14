# myapp/views.py

from django.shortcuts import render
from .models import Author, Book

def book_list(request):
    books = Book.objects.select_related('author')
    return render(request, 'myapp/book_list.html', {'books': books})
