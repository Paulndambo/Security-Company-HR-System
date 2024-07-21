# Generated by Django 5.0.6 on 2024-07-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_paymentconfig_job_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobrole",
            name="name",
        ),
        migrations.AddField(
            model_name="jobrole",
            name="category",
            field=models.CharField(
                choices=[("Staff", "Staff"), ("Service Provider", "Service Provider")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
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
                null=True,
            ),
        ),
    ]