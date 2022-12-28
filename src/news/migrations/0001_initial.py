# Generated by Django 4.0.5 on 2022-12-06 13:14

from django.db import migrations, models
import django.db.models.deletion
from typing import Any, List


class Migration(migrations.Migration):

    initial = True

    dependencies: List[Any] = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=150, unique=True)),
                ("author", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=150, unique=True)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_published", models.BooleanField(default=True)),
                ("views", models.PositiveIntegerField(default=0)),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="news.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]
