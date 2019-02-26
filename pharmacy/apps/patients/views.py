from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions as drf_permissions
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from pharmacy.apps.patients.serializers import PatientSerializer
from pharmacy.apps.patients.models import Patient
from pharmacy.apps.patients import forms as patient_forms


# Create your views here.
class PatientListCreateView(LoginRequiredMixin, ListCreateAPIView):
    permission_classes = (drf_permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PatientSerializer
    queryset = Patient.objects.all().order_by("name")


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = patient_forms.PatientForm
    success_url = reverse_lazy("index")
    template_name = "patients/patient_create.html"


class PatientListView(LoginRequiredMixin, ListView):
    queryset = Patient.objects.all().order_by("name")
    template_name = "patients/patients_list.html"


class PatientRetrieveUpdateView(LoginRequiredMixin, RetrieveUpdateAPIView):
    permission_classes = (drf_permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PatientSerializer
    queryset = Patient.objects.all().order_by("name")
