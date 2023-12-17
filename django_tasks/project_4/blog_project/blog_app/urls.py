# blog_app/urls.py

from django.urls import path
from .views import post_list, post_detail, create_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', create_post, name='create_post'),
 
]
