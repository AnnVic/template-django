# Generated by Django 4.0.5 on 2022-12-12 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="news.comment",
            ),
        ),
    ]
