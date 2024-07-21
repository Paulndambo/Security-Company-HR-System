from django.contrib import admin
from apps.payments.models import EmployeeOvertime, EmployeeSalary

# Register your models here.
admin.site.register(EmployeeOvertime)
admin.site.register(EmployeeSalary)
