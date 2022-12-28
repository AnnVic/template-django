# pylint: disable=too-many-ancestors
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import serializers
from news.permissions import IsAuthorOrReadOnly
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(
        self, serializer: serializers.BaseSerializer[CommentSerializer]
    ) -> None:
        serializer.save(author=self.request.user)
