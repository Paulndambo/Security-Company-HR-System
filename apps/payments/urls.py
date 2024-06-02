from django.urls import path
from apps.payments.views import employee_salaries, overtimes, record_overtime

urlpatterns = [
    path("salaries/", employee_salaries, name="salaries"),
    path("overtimes/", overtimes, name="overtimes"),
    path("record-overtime/", record_overtime, name="record-overtime"),
]