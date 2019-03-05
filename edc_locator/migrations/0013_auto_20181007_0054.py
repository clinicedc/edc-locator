# Generated by Django 2.1 on 2018-10-06 23:03

from django.db import migrations
from edc_action_item.data_fixers import fix_null_historical_action_identifier


def fix(apps, schema_editor):

    fix_null_historical_action_identifier(
        app_label="edc_locator", models=["subjectlocator"]
    )


class Migration(migrations.Migration):

    dependencies = [("edc_locator", "0012_auto_20181010_2121")]

    operations = [migrations.RunPython(fix)]