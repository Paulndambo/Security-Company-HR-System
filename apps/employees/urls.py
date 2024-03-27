from django.urls import path
from apps.employees.views import attendaces, new_attendance, generate_attendance

urlpatterns = [ 
    path("attendances/", attendaces, name="attendances"),
    path("new-attendance/", new_attendance, name="new-attendance"),
    path("generate-attendance/", generate_attendance, name="generate-attendance"),
]