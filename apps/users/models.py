from django.db import models
from apps.core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.
USER_ROLES = (
    ("Admin", "Admin"),
    ("Hr Admin", "Hr Admin"),
    ("Employee", "Employee"),
    ("Staff", "Staff"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)


EMPLOYEE_STATUS = (
    ("Pending Approval", "Pending Approval"),
    ("Declined", "Declined"),
    ("Available", "Available"),
    ("On Leave", "On Leave"),
    ("Suspended", "Suspended"),
)

EMPLOYMENT_POSITION_CHOICES = (
    ("Security Manager", "Security Manager"),
    ("Security Guard", "Security Guard"),
    ("CCTV Installer", "CCTV Installer"),
)


class User(AbstractBaseModel, AbstractUser):
    role = models.CharField(max_length=255, choices=USER_ROLES)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True)
    nhif_number = models.CharField(max_length=255, null=True)
    nssf_number = models.CharField(max_length=255, null=True)
    kra_pin = models.CharField(max_length=255, null=True)
    position = models.ForeignKey(
        "core.JobRole",
        on_delete=models.SET_NULL,
        null=True,
        related_name="staffpositions",
    )
    postal_address = models.CharField(max_length=255, null=True)
    physical_address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    basic_salary = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def employee_address(self):
        return f"{self.postal_address}, {self.town}-{self.country}"
