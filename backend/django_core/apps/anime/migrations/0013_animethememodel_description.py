# Generated by Django 4.2 on 2023-04-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0012_animethememodel_created_at_animethememodel_is_locked_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animethememodel",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
