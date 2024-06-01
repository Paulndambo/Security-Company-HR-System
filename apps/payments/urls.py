from django.urls import path
from apps.payments.views import employee_salaries, overtimes

urlpatterns = [
    path("salaries/", employee_salaries, name="salaries"),
    path("overtimes/", overtimes, name="overtimes"),
]