from django.urls import path
from pharmacy.apps.medicine import views as medicine_views


app_name = "medicine"

urlpatterns = [
    path("rest/", medicine_views.ListCreateAPIView.as_view(), name="medicine_list_create"),
    path("rest/<int:id>/", medicine_views.MedicineRetrieveUpdateView.as_view(), name="medicine_retrieve_update"),
    path("rest/search/", medicine_views.MedicineSearchView.as_view(), name="medicine_search"),

    path("list/", medicine_views.MedicineListView.as_view(), name="medicine_list"),
    path("create/", medicine_views.MedicineCreateView.as_view(), name="medicine_create")
]
