# Generated by Django 2.0.3 on 2018-04-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_locator", "0007_auto_20180117_1819")]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectlocator",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectlocator",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="subjectlocator",
            name="parent_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="subjectlocator",
            name="related_tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
