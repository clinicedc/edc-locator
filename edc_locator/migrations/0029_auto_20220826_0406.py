# Generated by Django 3.2.13 on 2022-08-26 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edc_locator", "0028_auto_20220826_0322"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalsubjectlocator",
            name="tracking_identifier",
        ),
        migrations.RemoveField(
            model_name="subjectlocator",
            name="tracking_identifier",
        ),
    ]