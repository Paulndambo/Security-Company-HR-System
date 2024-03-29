from django.urls import path
from apps.payments.views import employee_salaries

urlpatterns = [
    path("salaries/", employee_salaries, name="salaries"),
]