from typing import Any
from rest_framework import serializers
from .models import Category, Article


class ArticleSerializer(serializers.ModelSerializer[Article]):
    comments: "serializers.SlugRelatedField[Article]" = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="content"
    )

    class Meta:
        model = Article
        fields = (
            "title",
            "content",
            "created_at",
            "author",
            "views",
            "category_id",
            "comments",
        )
        read_only_fields = ("views",)

    def to_representation(self, instance: Article) -> Any:
        data = super().to_representation(instance)
        cat_name = Category.objects.get(pk=data["category_id"])
        data["category_id"] = cat_name.title
        return data


class CategorySerializer(serializers.ModelSerializer[Category]):
    articles: "serializers.SlugRelatedField[Category]" = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="title"
    )

    class Meta:
        model = Category
        fields = ("title", "articles")
