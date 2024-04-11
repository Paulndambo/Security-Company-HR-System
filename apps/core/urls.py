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
]
