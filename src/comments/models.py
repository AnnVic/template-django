from django.db import models
from django.contrib.auth import get_user_model
from news.models import Article

User = get_user_model()


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
        default=None,
    )
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")

    def __str__(self) -> str:
        return self.content
