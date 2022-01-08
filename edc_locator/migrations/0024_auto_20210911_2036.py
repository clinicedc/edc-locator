# Generated by Django 3.2.6 on 2021-09-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_locator', '0023_auto_20210203_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectlocator',
            name='tracking_identifier',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='subjectlocator',
            name='tracking_identifier',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]