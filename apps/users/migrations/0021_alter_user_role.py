# Generated by Django 5.0.6 on 2024-07-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0020_user_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("Admin", "Admin"),
                    ("Hr Admin", "Hr Admin"),
                    ("Employee", "Employee"),
                    ("Staff", "Staff"),
                ],
                max_length=255,
            ),
        ),
    ]