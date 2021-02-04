# Generated by Django 2.1.7 on 2019-03-04 23:23

import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.models.audit_model_mixin
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_locator", "0017_auto_20190114_0250")]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="created",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="hostname_modified",
            field=django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="modified",
            field=models.DateTimeField(
                blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
            ),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="user_created",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user created",
            ),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="user_modified",
            field=django_audit_fields.fields.userfield.UserField(
                blank=True,
                help_text="Updated by admin.save_model",
                max_length=50,
                verbose_name="user modified",
            ),
        ),
    ]
