# type: ignore
from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "article", "created", "active")
    list_filter = ("active", "created")
    search_fields = ("author", "article")


admin.site.register(Comment, CommentAdmin)
