# Generated by Django 5.0.3 on 2024-04-11 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "employees",
            "0020_rename_chief_letter_employeedocument_chief_letter_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="employeedocument",
            old_name="Chief Letter",
            new_name="chief_letter",
        ),
        migrations.RenameField(
            model_name="employeedocument",
            old_name="College Certificate",
            new_name="college_certificate",
        ),
        migrations.RenameField(
            model_name="employeedocument",
            old_name="KCPE Certificate",
            new_name="kcpe_certificate",
        ),
        migrations.RenameField(
            model_name="employeedocument",
            old_name="KCSE Certificate",
            new_name="kcse_certificate",
        ),
        migrations.RenameField(
            model_name="employeedocument",
            old_name="KRA Certificate",
            new_name="kra_certificate",
        ),
        migrations.RenameField(
            model_name="employeedocument",
            old_name="Police Clearance",
            new_name="police_clearance",
        ),
        migrations.RenameField(
            model_name="employeedocument",
            old_name="Referee Letter",
            new_name="referee_letter",
        ),
        migrations.RenameField(
            model_name="employeedocument",
            old_name="Scanned ID",
            new_name="scanned_id",
        ),
    ]
