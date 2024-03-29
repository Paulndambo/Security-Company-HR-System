from django.db import models
from apps.core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.
USER_ROLES = (
    ("Admin", "Admin"),
    ("Hr Admin", "Hr Admin"),
    ("Employee", "Employee"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)


EMPLOYMENT_POSITION_CHOICES = (
    ("Security Manager", "Security Manager"),
    ("Security Guard", "Security Guard"),
)


class User(AbstractBaseModel, AbstractUser):
    role = models.CharField(max_length=255, choices=USER_ROLES)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True)
    nhif_number = models.CharField(max_length=255, null=True)
    nssf_number = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, choices=EMPLOYMENT_POSITION_CHOICES)
    postal_address = models.CharField(max_length=255, null=True)
    physical_address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    basic_salary = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    police_clearance = models.FileField(
        upload_to="police_clearances/", null=True, blank=True
    )
    chief_letter = models.FileField(upload_to="chief_letters/", null=True, blank=True)
    recommendation_letter = models.FileField(
        upload_to="recommended_letters/", null=True, blank=True
    )
    scanned_id = models.FileField(upload_to="scanned_ids/", null=True, blank=True)
    passport_photo = models.ImageField(
        upload_to="passport_photos/", null=True, blank=True
    )
    workstation = models.ForeignKey("core.Workstation", on_delete=models.SET_NULL, null=True, related_name="workstationsguards")

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def employee_address(self):
        return f"{self.postal_address}, {self.town}-{self.country}"
