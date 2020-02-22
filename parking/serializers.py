from django.apps import apps
from django.conf import settings
from rest_framework import serializers
from .models import Vehicle, Slot, Parking


class VehicleSerializer(serializers.ModelSerializer):
    """
    Vehicle model Serializer
    """

    class Meta:
        model = Vehicle
        fields = ('registration_number', 'color')


class SlotSerializer(serializers.ModelSerializer):
    """
    Slot model Serializer
    """

    class Meta:
        model = Slot
        fields = ('position', 'status')


class ParkingSerializer(serializers.ModelSerializer):
    """
    Parking model Serializer
    """
    vehicle = VehicleSerializer(required=True)
    slot = SlotSerializer(required=True)

    class Meta:
        model = Parking
        fields = ('id', 'vehicle', 'slot')
