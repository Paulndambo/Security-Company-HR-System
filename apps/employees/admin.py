from django.contrib import admin
from apps.employees.models import EmployeeDocument
# Register your models here.
@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ["id", "employee", "police_clearance", "chief_letter", "referee_letter"]