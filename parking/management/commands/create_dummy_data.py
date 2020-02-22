import random

from django.conf import settings
from django.core.management.base import BaseCommand

from parking.models import Vehicle, Slot, Parking


class Command(BaseCommand):
    @staticmethod
    def generate_randon_registration_number(number_of_vehicles):
        """
        TO Generate random Registration number
        :param number_of_vehicles: Number of vehicles you entered
        :return: List of Registration number
        """
        return [
            "{}{}-{}{}-{}{}-{}{}{}{}".format(chr(random.randint(65, 90)), chr(random.randint(65, 90)),
                                             str(random.randrange(10)), str(random.randrange(10)),
                                             chr(random.randint(65, 90)), chr(random.randint(65, 90)),
                                             str(random.randrange(10)), str(random.randrange(10)),
                                             str(random.randrange(10)), str(random.randrange(10))) for _ in
            range(1, number_of_vehicles + 1)]

    def create_dumy_entry(self, number_of_slots, number_of_vehicles):
        """
        TO create the dummy data
        :param number_of_slots: Number of parking slots
        :param number_of_vehicles: Number of parked vehicles
        :return:
        """
        vehicle_colors = ["black", "white", "blue", "red"]
        # Create number of parking spaces
        Slot.objects.bulk_create([Slot(position=x) for x in range(1, number_of_slots + 1)])
        # Create number of Vehicle with random number and colors
        Vehicle.objects.bulk_create(
            [Vehicle(registration_number=number, color=random.choice(vehicle_colors)) for number in
             self.generate_randon_registration_number(number_of_vehicles)])
        # Parked number of vehicles in present slots
        for x in range(1, number_of_vehicles + 1):
            Parking.objects.create(vehicle_id=x, slot_id=x)
            # Updating particular slot status
            Slot.objects.filter(id=x).update(status=settings.STATUSES[1][0])

    def handle(self, *args, **options):
        print("Creating Dummy Data....")
        print("Enter number of parking spaces you want to create")
        number_of_slots = int(input())
        print("Enter number of cars currently in the parking lot")
        number_of_vehicles = int(input())
        self.create_dumy_entry(number_of_slots, number_of_vehicles)
        print("Data Created Successfully....")
