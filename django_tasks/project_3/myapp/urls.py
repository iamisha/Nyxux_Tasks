# myapp/urls.py

from django.urls import path
from .views import book_list

urlpatterns = [
    path('books/', book_list, name='book_list'),
    # Add more URL patterns as needed
]
