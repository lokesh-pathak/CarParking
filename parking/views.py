from django.shortcuts import render
from rest_framework import generics
from .models import Vehicle, Slot, Parking
from .serializers import ParkingSerializer, SlotSerializer, VehicleSerializer
# Create your views here.


class ParkingSerializerListView(generics.ListAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    pagination_class = None
