from django.db import models
from apps.core.models import AbstractBaseModel

# Create your models here.
STATUS_CHOICES = (
    ("Absent", "Absent"),
    ("Present", "Present"),
)


class Attendance(AbstractBaseModel):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    checkin_time = models.DateTimeField(auto_now_add=True, null=True)
    checkout_time = models.DateTimeField(null=True, blank=True)
    checked_in_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="checkinmanagers",
    )
    marked = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Present")

    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name
