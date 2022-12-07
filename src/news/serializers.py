from rest_framework import serializers
from .models import Category, Article


class ArticleSerializer(serializers.ModelSerializer):
    category_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = ("title", "content", "created_at", "author", "views",
                  "category_id")


class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("title", "articles")
