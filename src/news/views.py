# pylint: disable=too-many-ancestors
from typing import Any
from rest_framework import viewsets
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def retrieve(
        self, request: Any, *args: tuple[str], **kwargs: dict[str, Any]
    ) -> Response:
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=("views",))
        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
