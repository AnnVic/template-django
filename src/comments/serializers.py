# pylint: disable=abstract-method
from typing import Any
from rest_framework import serializers
from news.models import Article
from .models import Comment


class FilterCommentListSerializer(serializers.ListSerializer[Comment]):
    def to_representation(self, data: Any) -> Any:
        data = Comment.objects.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer[Comment]):
    def to_representation(self, instance: Comment) -> Any:
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer[Comment]):
    replies = RecursiveSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "article", "author", "content", "parent", "replies")
        read_only_fields = ("replies", "author")

    def to_representation(self, instance: Comment) -> Any:
        data = super().to_representation(instance)
        art_name = Article.objects.get(pk=data["article"])
        data["article"] = art_name.title
        return data
