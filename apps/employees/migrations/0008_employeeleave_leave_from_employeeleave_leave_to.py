# Generated by Django 5.0.3 on 2024-03-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0007_employeeleave"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeeleave",
            name="leave_from",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="employeeleave",
            name="leave_to",
            field=models.DateField(null=True),
        ),
    ]