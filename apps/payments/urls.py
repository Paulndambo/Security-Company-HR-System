from django.urls import path
from apps.payments.views import (employee_salaries, payslip_receipt, overtimes, record_overtime, payslips, generate_payslips, delete_payslip, new_bank_details,
    edit_bank_details,)

urlpatterns = [
    path("salaries/", employee_salaries, name="salaries"),
    path("overtimes/", overtimes, name="overtimes"),
    path("record-overtime/", record_overtime, name="record-overtime"),

    path("payslips/", payslips, name="payslips"),
    path("generate-payslips/", generate_payslips, name="generate-payslips"),
    path("delete-payslip/", delete_payslip, name="delete-payslip"),
    path("payslip-receipt/<int:id>/", payslip_receipt, name="payslip-receipt"),
    path("new-bank-details/", new_bank_details, name="new-bank-details"),
    path("edit-bank-details/", edit_bank_details, name="edit-bank-details"),
]