# Generated by Django 4.1.5 on 2023-01-12 14:39

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
            name="Planes",
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
                ("name", models.CharField(max_length=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("operator", models.CharField(max_length=50)),
                ("validity", models.DurationField()),
                ("description", models.CharField(max_length=255)),
                ("data", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Recharg",
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
                ("circle", models.CharField(max_length=150)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "selected_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recharge.planes",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]