# Generated by Django 5.0.3 on 2024-04-11 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_client_remove_workstation_contract_start_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="workstation",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="workstations",
                to="core.client",
            ),
        ),
    ]
