from django.shortcuts import render, redirect
from .models import Post, Comment, Tag
from .forms import PostForm


# Create your views here.


def post_list(request):
    # Use prefetch_related to minimize database hits
    posts = Post.objects.prefetch_related('comment_set', 'tags').all()
    return render(request, 'blog_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # Use prefetch_related to minimize database hits
    post = Post.objects.prefetch_related('comment_set', 'tags').get(pk=pk)
    return render(request, 'blog_app/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog_app/create_post.html', {'form': form})
