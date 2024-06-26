# Generated by Django 2.0.7 on 2018-07-08 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("edc_locator", "0008_auto_20180409_1009")]

    operations = [
        migrations.AlterModelOptions(
            name="historicalsubjectlocator",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Subject Locator",
            },
        ),
        migrations.RenameField(
            model_name="historicalsubjectlocator",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="historicalsubjectlocator",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
        migrations.RenameField(
            model_name="subjectlocator",
            old_name="parent_tracking_identifier",
            new_name="parent_reference_identifier",
        ),
        migrations.RenameField(
            model_name="subjectlocator",
            old_name="related_tracking_identifier",
            new_name="related_reference_identifier",
        ),
    ]
