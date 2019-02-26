from django.urls import path
from pharmacy.apps.patients import views as patient_views

app_name = "patients"

urlpatterns = [
    path("patients/", patient_views.PatientListCreateView.as_view(), name="patient_list_create"),
    path("patients/<int:id>/", patient_views.PatientRetrieveUpdateView.as_view(), name="patient_retrieve_update")
]
