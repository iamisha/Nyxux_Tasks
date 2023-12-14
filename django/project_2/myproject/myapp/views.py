# myapp/views.py

from django.shortcuts import render
from .models import Author, Book
from datetime import date

def home(request):
    # Dummy data for testing
    author1 = Author.objects.create(name='John Doe', bio='A mysterious author')
    author2 = Author.objects.create(name='Jane Smith', bio='An adventurous writer')

    Book.objects.create(title='Book 1', author=author1, published_date=date(2022, 1, 1))
    Book.objects.create(title='Book 2', author=author1, published_date=date(2022, 2, 1))
    Book.objects.create(title='Book 3', author=author2, published_date=date(2022, 3, 1))

    authors = Author.objects.all()
    books = Book.objects.all()
    return render(request, 'myapp/home.html', {'authors': authors, 'books': books})
