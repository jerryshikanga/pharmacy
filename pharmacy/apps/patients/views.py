from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions as drf_permissions

from pharmacy.apps.patients.serializers import PatientSerializer
from pharmacy.apps.patients.models import Patient


# Create your views here.
class PatientListCreateView(ListCreateAPIView):
    permission_classes = (drf_permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PatientSerializer
    queryset = Patient.objects.all().order_by("name")


class PatientRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = (drf_permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PatientSerializer
    queryset = Patient.objects.all().order_by("name")
