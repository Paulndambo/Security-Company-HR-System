from django.urls import path
from apps.employees.views import (
    attendaces,
    new_attendance,
    generate_attendance,
    mark_absent,
    mark_present,
    leave_applications,
    apply_leave,
    mark_attendance,
    reset_attendance,
    mark_leave_application,
    delete_leave_application,

    new_relative,
    edit_relative,
    delete_relative,

    new_education_record,
    edit_education_record,
    delete_education_record,

    new_bank_details,
    edit_bank_details,
)

urlpatterns = [
    path("attendances/", attendaces, name="attendances"),
    path("new-attendance/", new_attendance, name="new-attendance"),
    path("generate-attendance/", generate_attendance, name="generate-attendance"),
    path("mark-attendance/", mark_attendance, name="mark-attendance"),
    path(
        "reset-attendance/<int:attendance_id>/",
        reset_attendance,
        name="reset-attendance",
    ),
    path("mark-present/<int:attendance_id>/", mark_present, name="mark-present"),
    path("mark-absent/<int:attendance_id>/", mark_absent, name="mark-absent"),
    path("leave-applications/", leave_applications, name="leave-applications"),
    path("apply-leave/", apply_leave, name="apply-leave"),
    path("mark-leave/", mark_leave_application, name="mark-leave"),
    path("delete-leave/", delete_leave_application, name="delete-leave"),

    path("new-relative/", new_relative, name="new-relative"),
    path("edit-relative/", edit_relative, name="edit-relative"),
    path("delete-relative/", delete_relative, name="delete-relative"),

    path("new-education-record/", new_education_record, name="new-education-record"),
    path("edit-education-record/", edit_education_record, name="edit-education-record"),
    path("delete-education-record/", delete_education_record, name="delete-education-record"),

    path("new-bank-details/", new_bank_details, name="new-bank-details"),
    path("edit-bank-details/", edit_bank_details, name="edit-bank-details"),
]
