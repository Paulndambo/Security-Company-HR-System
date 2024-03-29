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
)

urlpatterns = [
    path("attendances/", attendaces, name="attendances"),
    path("new-attendance/", new_attendance, name="new-attendance"),
    path("generate-attendance/", generate_attendance, name="generate-attendance"),
    path("mark-attendance/", mark_attendance, name="mark-attendance"),
    path("reset-attendance/<int:attendance_id>/", reset_attendance, name="reset-attendance"),

    path("mark-present/<int:attendance_id>/", mark_present, name="mark-present"),
    path("mark-absent/", mark_absent, name="mark-absent"),

    path("leave-applications/", leave_applications, name="leave-applications"),
    path("apply-leave/", apply_leave, name="apply-leave"),
]
