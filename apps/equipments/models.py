from django.db import models
from apps.core.models import AbstractBaseModel

# Create your models here.
EQUIPMENT_TYPES = (
    ("Uniform", "Uniform"),
    ("Electronics", "Electronics"),
)

EQUIPMENT_ISSUE_STATUS = (
    ("Returned", "Returned"),
    ("Pending Return", "Pending Return"),
    ("Lost", "Lost"),
)


class Equipment(AbstractBaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    issued = models.IntegerField(default=0)
    category = models.CharField(max_length=255, choices=EQUIPMENT_TYPES)

    def __str__(self):
        return self.name


class EquipmentIssue(AbstractBaseModel):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    employee = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_issued = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    status = models.CharField(max_length=255, choices=EQUIPMENT_ISSUE_STATUS)
    issued_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="equipmentissuers",
    )

    def __str__(self):
        return self.equipment.name
