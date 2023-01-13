# Generated by Django 4.1.5 on 2023-01-13 03:42

import core.storages
import dynamic_filenames
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("characters", "0009_alter_charactermodel_character_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="charactermodel",
            name="character_image",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                storage=core.storages.OverwriteStorage(),
                upload_to=dynamic_filenames.FilePattern(
                    filename_pattern="anime_characters/{uuid:s}{ext}"
                ),
            ),
        ),
    ]
