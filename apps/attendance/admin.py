from django.contrib import admin
from apps.attendance.models import Attendance
# Register your models here.
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["id", "employee", "date", "checkin_time", "checked_in_by", "marked", "status"]
