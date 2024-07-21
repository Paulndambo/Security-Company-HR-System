from django.urls import path
from apps.leave.views import (
    leave_applications,
    apply_leave,
    mark_leave_application,
    delete_leave_application,
    complete_leave
)

urlpatterns = [
    path("leave-applications/", leave_applications, name="leave-applications"),
    path("apply-leave/", apply_leave, name="apply-leave"),
    path("mark-leave/", mark_leave_application, name="mark-leave"),
    path("complete-leave/", complete_leave, name="complete-leave"),
    path("delete-leave/", delete_leave_application, name="delete-leave"),
]