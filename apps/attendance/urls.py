from django.urls import path
from apps.attendance.views import (
    attendaces,
    generate_attendance,
    mark_absent,
    reset_attendance,
)

urlpatterns = [
    path("", attendaces, name="attendances"),
    path("generate-attendance/", generate_attendance, name="generate-attendance"),
    path("reset-attendance/<int:id>/", reset_attendance, name="reset-attendance"),
    path("mark-absent/<int:id>/", mark_absent, name="mark-absent"),
]
