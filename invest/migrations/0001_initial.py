# Generated by Django 4.2.7 on 2023-12-05 17:41

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
            name="Deposit",
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
                ("deposit", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "profit",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
                ),
                (
                    "plan",
                    models.CharField(
                        choices=[
                            ("starter", "STARTER PLAN"),
                            ("silver", "SILVER PLAN"),
                            ("gold", "GOLD PLAN"),
                            ("vip", "VIP PLAN"),
                            ("vip-platinum", "VIP PLATINUM PLAN"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "PENDING"), ("successful", "SUCCESSFUL")],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "gateway",
                    models.CharField(
                        choices=[("ethereum", "ETHEREUM"), ("bitcoin", "BITCOIN")],
                        default="ethereum",
                        max_length=20,
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="deposits",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
