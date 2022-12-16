# Generated by Django 4.1.4 on 2022-12-16 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PhotoPeopleName",
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
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
            ],
            options={
                "verbose_name": "Имя человека на фотографии",
                "verbose_name_plural": "Имена людей на фотографиях",
            },
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("photo", models.ImageField(upload_to="photos/")),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Гео локация",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Дата")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "people_names",
                    models.ManyToManyField(blank=True, to="photos.photopeoplename"),
                ),
            ],
            options={
                "verbose_name": "Фотография",
                "verbose_name_plural": "Фотографии",
            },
        ),
    ]
