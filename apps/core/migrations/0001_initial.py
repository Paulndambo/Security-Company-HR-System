# Generated by Django 5.0.3 on 2024-03-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Workstation",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("contract_start_date", models.DateField(blank=True, null=True)),
                (
                    "location_description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("guards_posted", models.IntegerField(default=0)),
                ("guards_needed", models.IntegerField(default=0)),
                (
                    "work_shift",
                    models.CharField(
                        choices=[
                            ("Day Shift", "Day Shift"),
                            ("Night Shift", "Night Shift"),
                            ("24 Hours Shift", "24 Hours Shift"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]