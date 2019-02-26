from django.urls import path
from pharmacy.apps.medicine import views as medicine_views


app_name = "medicine"

urlpatterns = [
    path("medicine/", medicine_views.ListCreateAPIView.as_view(), name="medicine_list_create"),
    path("medicine/<int:id>/", medicine_views.MedicineRetrieveUpdateView.as_view(), name="medicine_retrieve_update"),
    path("medicine/search/", medicine_views.MedicineSearchView.as_view(), name="medicine_search")
]
