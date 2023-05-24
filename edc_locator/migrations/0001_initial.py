# Generated by Django 2.0 on 2018-01-02 22:00

import _socket
import django.contrib.sites.managers
import django.db.models.deletion
import django.db.models.manager
import django_audit_fields.fields.uuid_auto_field
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_revision.revision_field
import edc_model.validators.phone
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
import edc_utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalSubjectLocator",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "user_created",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "subject_identifier",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Subject Identifier"
                    ),
                ),
                ("tracking_identifier", models.CharField(db_index=True, max_length=30)),
                ("action_identifier", models.CharField(max_length=25, null=True)),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "may_call",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the participant given permission <b>to contacted by telephone or cell</b> by study staff for follow-up purposes during the study?",
                    ),
                ),
                (
                    "may_visit_home",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the participant given permission for studystaff <b>to make home visits</b> for follow-up purposes?",
                    ),
                ),
                (
                    "may_sms",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="Has the participant given permission <b>to be contacted by SMS</b> by study staff for follow-up purposes during the study?",
                    ),
                ),
                (
                    "mail_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Mailing address ",
                    ),
                ),
                (
                    "physical_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Physical address with detailed description",
                    ),
                ),
                (
                    "subject_cell",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number",
                    ),
                ),
                (
                    "subject_cell_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number (alternate)",
                    ),
                ),
                (
                    "subject_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone",
                    ),
                ),
                (
                    "subject_phone_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone (alternate)",
                    ),
                ),
                (
                    "subject_work_place",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=250,
                        null=True,
                        verbose_name="Name and location of work place",
                    ),
                ),
                (
                    "subject_work_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Work contact number ",
                    ),
                ),
                (
                    "may_contact_indirectly",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="For example a partner, spouse, family member, neighbour ...",
                        max_length=25,
                        verbose_name="Has the participant given permission for study staff <b>to contact anyone else</b> for follow-up purposes during the study?",
                    ),
                ),
                (
                    "indirect_contact_name",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Full names of the contact person",
                    ),
                ),
                (
                    "indirect_contact_relation",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Relationship to participant",
                    ),
                ),
                (
                    "indirect_contact_physical_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Full physical address ",
                    ),
                ),
                (
                    "indirect_contact_cell",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number",
                    ),
                ),
                (
                    "indirect_contact_cell_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number (alternative)",
                    ),
                ),
                (
                    "indirect_contact_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone number",
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(default=edc_utils.date.get_utcnow),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical ",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
        ),
        migrations.CreateModel(
            name="SubjectLocator",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_utils.date.get_utcnow),
                ),
                (
                    "user_created",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_model_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "subject_identifier",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Subject Identifier"
                    ),
                ),
                ("tracking_identifier", models.CharField(max_length=30, unique=True)),
                ("action_identifier", models.CharField(max_length=25, null=True)),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "may_call",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the participant given permission <b>to contacted by telephone or cell</b> by study staff for follow-up purposes during the study?",
                    ),
                ),
                (
                    "may_visit_home",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the participant given permission for studystaff <b>to make home visits</b> for follow-up purposes?",
                    ),
                ),
                (
                    "may_sms",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="Has the participant given permission <b>to be contacted by SMS</b> by study staff for follow-up purposes during the study?",
                    ),
                ),
                (
                    "mail_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Mailing address ",
                    ),
                ),
                (
                    "physical_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Physical address with detailed description",
                    ),
                ),
                (
                    "subject_cell",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number",
                    ),
                ),
                (
                    "subject_cell_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number (alternate)",
                    ),
                ),
                (
                    "subject_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone",
                    ),
                ),
                (
                    "subject_phone_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone (alternate)",
                    ),
                ),
                (
                    "subject_work_place",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=250,
                        null=True,
                        verbose_name="Name and location of work place",
                    ),
                ),
                (
                    "subject_work_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Work contact number ",
                    ),
                ),
                (
                    "may_contact_indirectly",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="For example a partner, spouse, family member, neighbour ...",
                        max_length=25,
                        verbose_name="Has the participant given permission for study staff <b>to contact anyone else</b> for follow-up purposes during the study?",
                    ),
                ),
                (
                    "indirect_contact_name",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Full names of the contact person",
                    ),
                ),
                (
                    "indirect_contact_relation",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Relationship to participant",
                    ),
                ),
                (
                    "indirect_contact_physical_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Full physical address ",
                    ),
                ),
                (
                    "indirect_contact_cell",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number",
                    ),
                ),
                (
                    "indirect_contact_cell_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number (alternative)",
                    ),
                ),
                (
                    "indirect_contact_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone number",
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(default=edc_utils.date.get_utcnow),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sites.Site",
                    ),
                ),
            ],
            options={"abstract": False},
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
