from django.urls import path
from apps.core.views import home, workstations, new_workstation, edit_workstation, delete_workstation, workstation_detail

urlpatterns = [
    path("", home, name="home"),
    path("workstations", workstations, name="workstations"),
    path("workstation/<int:workstation_id>", workstation_detail, name="workstation-detail"),
    path("edit-workstation", edit_workstation, name="edit-workstation"),
    path("delete-workstation", delete_workstation, name="delete-workstation"),
    path("new-workstation", new_workstation, name="new-workstation"),

]
