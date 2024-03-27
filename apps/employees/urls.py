from django.urls import path
from apps.employees.views import attendaces, new_attendance, generate_attendance, mark_absent, mark_present

urlpatterns = [ 
    path("attendances/", attendaces, name="attendances"),
    path("new-attendance/", new_attendance, name="new-attendance"),
    path("generate-attendance/", generate_attendance, name="generate-attendance"),
    path("mark-present/<int:attendance_id>/", mark_present, name="mark-present"),
    path("mark-absent/", mark_absent, name="mark-absent"),
]