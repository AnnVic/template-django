from django.contrib import admin
from .models import Category, Article, Comment

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "created_at", "views")
    list_filter = ("author", "is_published", "views", "created_at")
    ordering = ("is_published", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'article', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('author', 'article')


admin.site.register(Comment, CommentAdmin)