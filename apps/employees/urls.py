from django.urls import path
from apps.employees.views import (
    employees,
    new_employee,
    edit_employee,
    delete_employee,
    employee_details,
    upload_documents,
    approve_employee,
    disapprove_employee,
    new_relative,
    edit_relative,
    delete_relative,

    new_education_record,
    edit_education_record,
    delete_education_record,
)

urlpatterns = [
    path("", employees, name="employees"),
    path("new-employee/", new_employee, name="new-employee"),
    path("<int:employee_id>", employee_details, name="employee-details"),
    path("edit-employee/", edit_employee, name="edit-employee"),
    path("delete/", delete_employee, name="delete-employee"),
    path("upload-documents/", upload_documents, name="upload-documents"),
    path("approve-employee/", approve_employee, name="approve-employee"),
    path("disapprove-employee/", disapprove_employee, name="disapprove-employee"),

    path("new-relative/", new_relative, name="new-relative"),
    path("edit-relative/", edit_relative, name="edit-relative"),
    path("delete-relative/", delete_relative, name="delete-relative"),

    path("new-education-record/", new_education_record, name="new-education-record"),
    path("edit-education-record/", edit_education_record, name="edit-education-record"),
    path("delete-education-record/", delete_education_record, name="delete-education-record"),
]
