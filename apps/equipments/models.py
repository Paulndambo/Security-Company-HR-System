from django.db import models
from apps.core.models import AbstractBaseModel

# Create your models here.
EQUIPMENT_TYPES = (
    ("Shirt", "Shirt"),
    ("Head Cap", "Head Cap"),
    ("Belt", "Belt"),
    ("Trousers", "Trousers"),
    ("Chest Guard", "Chest Guard"),
    ("Shoes", "Shoes"),
    ("Boots", "Boots"),
    ("Sweater", "Sweater"),
    ("Baton", "Baton"),
)

EQUIPMENT_ISSUE_STATUS = (
    ("Returned", "Returned"),
    ("Pending Return", "Pending Return"),
    ("Lost", "Lost"),
    ("Returned Late", "Returned Late"),
)

EQUIPMENT_CONDITION_CHOICES = (
    ("New", "New"),
    ("Used", "Used"),
    ("Faulty", "Faulty"),
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
    employee = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    date_issued = models.DateField(null=True)
    issued_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="equipmentissuers",
    )
    head_cap_issued = models.BooleanField(default=False)
    shirt_issued = models.BooleanField(default=False)
    belt_issued = models.BooleanField(default=False)
    chest_guard_issued = models.BooleanField(default=False)
    shoes_issued = models.BooleanField(default=False)
    boots_issued = models.BooleanField(default=False)
    sweater_issued = models.BooleanField(default=False)
    baton_issued = models.BooleanField(default=False)
    trouser_issued = models.BooleanField(default=False)



    def __str__(self):
        return self.equipment.name


class EquipmentLog(AbstractBaseModel):
    equipment = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    actioned_by = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)


class EquipmentIssueLog(AbstractBaseModel):
    equipment_issue = models.ForeignKey(EquipmentIssue, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    actioned_by = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
