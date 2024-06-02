from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
MONTHS_LIST = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

class EmployeeSalary(AbstractBaseModel):
    employee = models.ForeignKey("users.User", on_delete=models.CASCADE)
    month = models.CharField(max_length=255, choices=MONTHS_LIST)
    year = models.CharField(max_length=10)
    days_worked = models.IntegerField(default=0)
    daily_rate = models.DecimalField(max_digits=100, decimal_places=2)
    overtime = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name
    

class EmployeeOvertime(AbstractBaseModel):
    employee = models.ForeignKey("users.User", on_delete=models.CASCADE)
    month = models.CharField(max_length=255, choices=MONTHS_LIST)
    year = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    overtime_date = models.DateField()

    def __str__(self):
        return self.year + "-" + self.month