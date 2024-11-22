# Generated by Django 4.2.16 on 2024-11-22 17:41

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
            name="Discipline",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
            ],
            options={
                "verbose_name": "дисциплина",
                "verbose_name_plural": "дисциплины",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
            ],
            options={
                "verbose_name": "наименование спортивного мероприятия",
                "verbose_name_plural": "наименования спортивного мероприятия",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Structure",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
            ],
            options={
                "verbose_name": "состав",
                "verbose_name_plural": "составы",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Tip",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
            ],
            options={
                "verbose_name": "тип соревнования",
                "verbose_name_plural": "типы соревнований",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Meropriation",
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
                ("slug", models.SlugField(max_length=200, verbose_name="слаг")),
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
                ("text", models.TextField(verbose_name="текст")),
                (
                    "count",
                    models.PositiveIntegerField(verbose_name="количество участников"),
                ),
                ("place", models.TextField(verbose_name="место проведения")),
                (
                    "date_start",
                    models.DateTimeField(null=True, verbose_name="дата начала"),
                ),
                (
                    "date_end",
                    models.DateTimeField(null=True, verbose_name="дата конца"),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="catalog_items",
                        to="meropriations.group",
                        verbose_name="категория",
                    ),
                ),
                (
                    "structure",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="catalog_items",
                        to="meropriations.structure",
                        verbose_name="категория",
                    ),
                ),
                (
                    "tip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="catalog_items",
                        to="meropriations.tip",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "мероприятие",
                "verbose_name_plural": "мероприятия",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="CustomRequest",
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
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="название"
                    ),
                ),
                (
                    "disciplines",
                    models.ManyToManyField(
                        to="meropriations.discipline", verbose_name="дисциплины"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "дисциплина",
                "verbose_name_plural": "дисциплины",
                "ordering": ("name",),
            },
        ),
    ]
