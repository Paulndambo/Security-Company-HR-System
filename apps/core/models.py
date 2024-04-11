from django.db import models


# Create your models here.
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


SHIFT_CHOICES = (
    ("Day Shift", "Day Shift"),
    ("Night Shift", "Night Shift"),
    ("24 Hours Shift", "24 Hours Shift"),
)


class Client(AbstractBaseModel):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    contract_start_date = models.DateField(null=True, blank=True)
    location_description = models.CharField(max_length=500, null=True, blank=True)
    guards_posted = models.IntegerField(default=0)
    guards_needed = models.IntegerField(default=0)
    work_shift = models.CharField(max_length=255, choices=SHIFT_CHOICES)
    postal_address = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Workstation(AbstractBaseModel):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name="workstations")
    name = models.CharField(max_length=255)
    guards_posted = models.IntegerField(default=0)
    guards_needed = models.IntegerField(default=0)
    work_shift = models.CharField(max_length=255, choices=SHIFT_CHOICES)
    

    def __str__(self):
        return self.name
