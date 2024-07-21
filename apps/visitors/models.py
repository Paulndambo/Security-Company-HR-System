from django.db import models
from apps.core.models import AbstractBaseModel


# Create your models here.
class Visitor(AbstractBaseModel):
    place = models.ForeignKey("core.Client", on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, null=True)
    office_visiting = models.CharField(max_length=500, null=True)
    visitation_reason = models.CharField(max_length=1000, null=True)
    car_plate_number = models.CharField(max_length=255, null=True)
    car_model = models.CharField(max_length=255, null=True)
    car_colour = models.CharField(max_length=255, null=True)


class Visit(AbstractBaseModel):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.visitor.first_name
