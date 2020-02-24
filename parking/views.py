from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView

from .forms import VehicleForm
from .models import Vehicle, Slot, Parking


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'parked_vehicle_list'

    def get_queryset(self):
        """Return the allotted parked vehicles """
        return Parking.objects.filter(vehicle__in=Vehicle.objects.filter(
            Q(registration_number__iexact=self.request.GET.get('search')) | Q(
                color__iexact=self.request.GET.get('search')))).order_by('-id') if self.request.GET.get(
            'search') else Parking.objects.all().order_by('-id')


class VehicleEntryView(FormView):
    template_name = 'vehicle.html'
    form_class = VehicleForm
    success_url = '/'

    def form_valid(self, form):
        """
        TO display empty from to create vehicle entry
        :param form:
        :return: Empty form
        """
        form.send_email()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """
        To create Parking Entry
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            vehicle = form.save()
            # To get nearest empty slot
            slot = Slot.objects.filter(status=settings.STATUSES[0][0]).first()
            # Allot parking slot to particular vehicle
            Parking.objects.create(vehicle=vehicle, slot=slot)
            # To update slot status from available to occupied
            slot.status = settings.STATUSES[1][0]
            slot.save()
            return HttpResponseRedirect('/index/')
        else:
            raise ValueError(form.errors)


def vehicle_exiting(request):
    """
    To delete Vehicle entry and empty the parking slot
    :param request:
    :return:
    """
    if 'id' in request.GET:
        # Mark given vehicle slot to available
        Slot.objects.filter(
            id__in=Parking.objects.filter(vehicle_id=int(request.GET.get('id'))).values_list('slot_id')).update(
            status=settings.STATUSES[0][0])
        # To delete the vehicle entry
        Vehicle.objects.filter(id=request.GET.get('id')).delete()
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/index/')
