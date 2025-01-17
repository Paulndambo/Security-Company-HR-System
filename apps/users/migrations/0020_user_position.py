# Generated by Django 5.0.6 on 2024-06-05 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_taxband"),
        ("users", "0019_remove_user_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="position",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jobpositions",
                to="core.paymentconfig",
            ),
        ),
    ]
