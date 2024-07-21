from django.urls import path
from apps.equipments.views import (
    equipments,
    new_equipment,
    edit_equipment,
    delete_equipment,
    issued_equipment,
    issue_equipment,
    delete_issued_equipment,
    mark_issued_equipment,
    vehicles,
    new_vehicle,
    edit_vehicle,
    delete_vehicle,
    vehicle_fueling_history,
    vehicle_service_history,
)

urlpatterns = [
    path("", equipments, name="equipments"),
    path("new-equipment", new_equipment, name="new-equipment"),
    path("edit-equipment", edit_equipment, name="edit-equipment"),
    path("delete-equipment", delete_equipment, name="delete-equipment"),
    path("issued-equipments", issued_equipment, name="issued-equipments"),
    path("issue-equipment", issue_equipment, name="issue-equipment"),
    path("mark-issued-equipment", mark_issued_equipment, name="mark-issued-equipment"),
    path(
        "delete-issued-equipment",
        delete_issued_equipment,
        name="delete-issued-equipment",
    ),
    path("vehicles/", vehicles, name="vehicles"),
    path("new-vehicle/", new_vehicle, name="new-vehicle"),
    path("edit-vehicle/", edit_vehicle, name="edit-vehicle"),
    path("delete-vehicle/", delete_vehicle, name="delete-vehicle"),
    path("vehicles/<int:id>/fueling-history/", vehicle_fueling_history, name="fueling-history"),
    path("vehicles/<int:id>/service-history/", vehicle_service_history, name="servicing-history"),
]
