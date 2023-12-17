from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
