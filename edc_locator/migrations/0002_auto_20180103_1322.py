# Generated by Django 2.0 on 2018-01-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_locator", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="subjectlocator", options={"verbose_name": "Subject Locator"}
        ),
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="may_visit_home",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                verbose_name="Has the participant given permission for study staff <b>to make home visits</b> for follow-up purposes?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="may_visit_home",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                verbose_name="Has the participant given permission for study staff <b>to make home visits</b> for follow-up purposes?",
            ),
        ),
    ]
