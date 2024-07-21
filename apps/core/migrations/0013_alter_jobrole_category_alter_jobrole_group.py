# Generated by Django 5.0.6 on 2024-07-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_remove_jobrole_name_jobrole_category_jobrole_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobrole",
            name="category",
            field=models.CharField(
                choices=[("Staff", "Staff"), ("Service Provider", "Service Provider")],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="jobrole",
            name="group",
            field=models.CharField(
                choices=[
                    ("Security Manager", "Security Manager"),
                    ("Supervisor", "Supervisor"),
                    ("Finance Officer", "Finance Officer"),
                    ("HR Admin", "HR Admin"),
                    ("Security Guard", "Security Guard"),
                    ("CCTV Installer", "CCTV Installer"),
                ],
                max_length=255,
            ),
        ),
    ]