from django.urls import path
from apps.users.views import user_login, user_logout, employees, new_employee

urlpatterns = [ 
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    # Employee urls
    path("employees/", employees, name="employees"),
    path("new-employee/", new_employee, name="new-employee"),
]