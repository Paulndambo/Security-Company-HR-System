# Generated by Django 5.0.3 on 2024-04-09 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0018_employeedocument"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employeedocument",
            old_name="recommendation_letter",
            new_name="referee_letter",
        ),
    ]