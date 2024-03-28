from django.urls import path
from apps.equipments.views import equipments, new_equipment, edit_equipment, delete_equipment, issued_equipment, issue_equipment

urlpatterns = [
    path("", equipments, name="equipments"),
    path("new-equipment", new_equipment, name="new-equipment"),
    path("edit-equipment", edit_equipment, name="edit-equipment"),
    path("delete-equipment", delete_equipment, name="delete-equipment"),
    path("issued-equipments", issued_equipment, name="issued-equipments"),
    path("issue-equipment", issue_equipment, name="issue-equipment"),
]   