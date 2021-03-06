from django.contrib import admin
from .models import Post, Comment
# Register your models here.

# admin.site.register (Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "view_count",
        "created_at",
        "image",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
    )