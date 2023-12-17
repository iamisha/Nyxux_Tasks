from django.contrib import admin
from .models import Post, Comment, Tag
# Register your models here.


from django.contrib import admin


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date',)
    search_fields = ('title', 'author',)
    inlines = [CommentInline]
    filter_horizontal = ('tags',)

admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
