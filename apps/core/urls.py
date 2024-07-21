from django.urls import path
from apps.core.views import (
    home,
    clients,
    new_client,
    edit_client,
    delete_client,
    client_detail,

    new_workstation,
    edit_workstation,
    delete_workstation,

    payments,
    new_payment_config,
    edit_payment_config,
    delete_payment_config,

    tax_configurations,
    new_tax_config,
    edit_tax_config,
    delete_tax_config,

    job_roles,
    new_job_role,
    edit_job_role,
    delete_job_role
)

urlpatterns = [
    path("", home, name="home"),
    path("clients", clients, name="clients"),
    path("clients/<int:client_id>",client_detail,name="client-detail"),
    path("edit-client", edit_client, name="edit-client"),
    path("delete-client", delete_client, name="delete-client"),
    path("new-client", new_client, name="new-client"),

    path("new-workstation", new_workstation, name="new-workstation"),
    path("edit-workstation", edit_workstation, name="edit-workstation"),
    path("delete-workstation", delete_workstation, name="delete-workstation"),

    path("job-roles/", job_roles, name="job-roles"),
    path("new-job-role/", new_job_role, name="new-job-role"),
    path("edit-job-role/", edit_job_role, name="edit-job-role"),
    path("delete-job-role/", delete_job_role, name="delete-job-role"),

    path("payment-configs/", payments, name="payment-configs"),
    path("new-payment-config/", new_payment_config, name="new-payment-config"),
    path("edit-payment-config/", edit_payment_config, name="edit-payment-config"),
    path("delete-payment-config/", delete_payment_config, name="delete-payment-config"),

    path("tax-configurations/", tax_configurations, name="tax-configurations"),
    path("new-tax-config/", new_tax_config, name="new-tax-config"),
    path("edit-tax-config/", edit_tax_config, name="edit-tax-config"),
    path("delete-tax-config/", delete_tax_config, name="delete-tax-config"),
]
