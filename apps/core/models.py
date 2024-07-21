from django.db import models


# Create your models here.
SP_CATEGORIES_CHOICES = (
    ("Staff", "Staff"),
    ("Service Provider", "Service Provider"),
)
SP_GROUP_CHOICES = (
    ("Security Manager", "Security Manager"),
    ("Supervisor", "Supervisor"),
    ("Finance Officer", "Finance Officer"),
    ("HR Admin", "HR Admin"),
    ("Security Guard", "Security Guard"),
    ("CCTV Installer", "CCTV Installer"),
)

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

TAX_BANDS = (
    ("1st Band", "1st Band"),
    ("2nd Band", "2nd Band"),
    ("3rd Band", "3rd Band"),
)

class TaxBand(AbstractBaseModel):
    category = models.CharField(max_length=255, choices=TAX_BANDS)
    lower_end = models.DecimalField(max_digits=100, decimal_places=2)
    upper_end = models.DecimalField(max_digits=100, decimal_places=2)
    nhif = models.DecimalField(max_digits=100, decimal_places=2)
    shif = models.DecimalField(max_digits=100, decimal_places=2)
    nssf_tier_one = models.DecimalField(max_digits=100, decimal_places=2)
    nssf_tier_two = models.DecimalField(max_digits=100, decimal_places=2)
    housing_levy = models.DecimalField(max_digits=10, decimal_places=2)
    tax_relief = models.DecimalField(max_digits=10, decimal_places=2)
    allowable_deductions = models.DecimalField(max_digits=100, decimal_places=2)
    insurance_relief = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.category
    

class JobRole(AbstractBaseModel):
    category = models.CharField(max_length=255, choices=SP_CATEGORIES_CHOICES)
    group = models.CharField(max_length=255, choices=SP_GROUP_CHOICES)

    def __str__(self):
        return self.name
    

class PaymentConfig(AbstractBaseModel):
    job_group = models.ForeignKey(JobRole, on_delete=models.SET_NULL, null=True)
    monthly_rate = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    daily_rate = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    overtime = models.DecimalField(max_digits=100, decimal_places=0, default=0)

    def __str__(self):
        return self.job_group.name