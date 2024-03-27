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
    position = models.CharField(max_length=255, choices=EMPLOYMENT_POSITION_CHOICES)
    postal_address = models.CharField(max_length=255, null=True)
    physical_address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
    @property
    def employee_address(self):
        return f"{self.postal_address}, {self.town}-{self.country}"
    