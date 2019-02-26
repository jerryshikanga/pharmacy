from django.urls import path

from pharmacy.apps.prescriptions import views


app_name = "prescriptions"

urlpatterns = [
    path("create/", views.PrecriptionCreateView.as_view(), name="prescription_create"),
    path("list/", views.PrescriptionListView.as_view(), name="prescription_list")
]