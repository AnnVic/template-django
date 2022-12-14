from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Article(models.Model):
    category_id = models.ForeignKey(Category,
                                    related_name="articles",
                                    on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name="comments")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    parent = models.ForeignKey("self",
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name="replies",
                               default=None)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    liked = models.ManyToManyField(User,
                                   default=None,
                                   blank=True,
                                   related_name="liked")

    def __str__(self) -> str:
        return self.content
