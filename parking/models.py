from django.db import models
from django.conf import settings


# Create your models here.
class Vehicle(models.Model):
    registration_number = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'vehicle'


class Slot(models.Model):
    position = models.IntegerField(blank=True, null =True)
    status = models.CharField(max_length=12, choices=settings.STATUSES, default=settings.STATUSES[0][0])

    class Meta:
        db_table = 'slot'


class Parking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)

    class Meta:
        db_table = 'parking'
