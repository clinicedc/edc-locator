#!/usr/bin/env python
import logging
from pathlib import Path

from edc_test_utils import DefaultTestSettings, func_main

app_name = "edc_locator"
base_dir = Path(__file__).absolute().parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    template_dirs=[str(base_dir / app_name / "tests" / "templates")],
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=str(base_dir / app_name / "tests" / "etc"),
    SUBJECT_VISIT_MODEL="edc_visit_tracking.subjectvisit",
    EDC_SITES_REGISTER_DEFAULT=True,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "simple_history",
        "django_crypto_fields.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_crf.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_locator.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
).settings


def main():
    func_main(project_settings, *[f"{app_name}.tests"])


if __name__ == "__main__":
    logging.basicConfig()
    main()
