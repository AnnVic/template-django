from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
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
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
