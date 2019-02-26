from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from pharmacy.apps.prescriptions.forms import PrescriptionForm
from pharmacy.apps.prescriptions.models import Prescription


# Create your views here.
class PrecriptionCreateView(LoginRequiredMixin, CreateView):
    form_class = PrescriptionForm
    success_url = reverse_lazy("prescriptions:prescription_list")
    template_name = "prescriptions/prescription_create_form.html"


class PrescriptionListView(LoginRequiredMixin, ListView):
    queryset = Prescription.objects.all().order_by("-id")
    template_name = "prescriptions/prescription_list.html"
