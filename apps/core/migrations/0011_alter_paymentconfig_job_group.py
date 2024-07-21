# Generated by Django 5.0.6 on 2024-07-21 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_jobrole"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentconfig",
            name="job_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.jobrole",
            ),
        ),
    ]
