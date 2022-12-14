from rest_framework import serializers
from .models import Category, Article, Comment
from django.contrib.auth.models import User
from typing import Any


class FilterCommentListSerializer(serializers.ListSerializer):

    def to_representation(self, data: Any) -> Any:
        data = Comment.objects.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value: Any) -> Any:
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer[Comment]):
    replies = RecursiveSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "article", "author", "content", "parent", "replies")
        read_only_fields = ("replies", "author")

    def to_representation(self, obj: Any) -> Any:
        data = super().to_representation(obj)
        art_name = Article.objects.get(pk=data["article"])
        data["article"] = art_name.title
        return data


class ArticleSerializer(serializers.ModelSerializer[Article]):
    comments = serializers.SlugRelatedField(many=True,
                                            read_only=True,
                                            slug_field="content")

    class Meta:
        model = Article
        fields = ("title", "content", "created_at", "author", "views",
                  "category_id", "comments")
        read_only_fields = ("views", )

    def to_representation(self, obj: Any) -> Any:
        data = super().to_representation(obj)
        cat_name = Category.objects.get(pk=data["category_id"])
        data["category_id"] = cat_name.title
        return data


class CategorySerializer(serializers.ModelSerializer[Category]):
    articles = serializers.SlugRelatedField(many=True,
                                            read_only=True,
                                            slug_field="title")

    class Meta:
        model = Category
        fields = ("title", "articles")
