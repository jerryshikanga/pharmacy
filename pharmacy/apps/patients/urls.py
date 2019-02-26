from django.urls import path
from pharmacy.apps.patients import views as patient_views

app_name = "patients"

urlpatterns = [
    path("rest/", patient_views.PatientListCreateView.as_view(), name="patient_list_create"),
    path("rest/<int:id>/", patient_views.PatientRetrieveUpdateView.as_view(), name="patient_retrieve_update"),
    path("list/", patient_views.PatientListView.as_view(), name="list_view"),
    path("create/", patient_views.PatientCreateView.as_view(), name="create_views")
]
