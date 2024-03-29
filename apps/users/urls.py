from django.urls import path
from apps.users.views import (
    user_login,
    user_logout,
    employees,
    new_employee,
    edit_employee,
    delete_employee,
    employee_details,
)

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    # Employee urls
    path("employees/", employees, name="employees"),
    path("new-employee/", new_employee, name="new-employee"),
    path("<int:employee_id>", employee_details, name="employee-details"),
    path("edit-employee/", edit_employee, name="edit-employee"),
    path("delete/<int:employee_id>", delete_employee, name="delete-employee"),
]
