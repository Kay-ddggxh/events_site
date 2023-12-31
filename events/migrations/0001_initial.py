# Generated by Django 4.2.7 on 2023-12-30 19:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UpcomingEvent",
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
                ("location", models.CharField(max_length=300)),
                ("venue", models.CharField(max_length=300)),
                ("datetime", models.DateTimeField()),
                ("admission", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "max_tickets",
                    models.IntegerField(
                        validators=[django.core.validators.MaxValueValidator(10000)]
                    ),
                ),
                ("cancelled", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        default="not found",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="event_uploader",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
