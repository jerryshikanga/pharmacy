from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import permissions as drf_permissions
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from pharmacy.apps.medicine import serializers
from pharmacy.apps.medicine.models import Medicine
from pharmacy.apps.medicine import forms as medicine_forms


# Create your views here.
class MedicineSearchView(APIView):
    permission_classes = (drf_permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = serializers.MedicineSearchSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.search_medicine()
            return Response(status=200, data=data)
        else:
            return Response(status=400, data=serializer.errors)


class MedicineListCreateView(ListCreateAPIView):
    serializer_class = serializers.MedicineSerializer
    permission_classes = (drf_permissions.IsAuthenticatedOrReadOnly,)
    queryset = Medicine.objects.all().order_by("name")


class MedicineRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = serializers.MedicineSerializer
    permission_classes = (drf_permissions.IsAuthenticatedOrReadOnly,)
    queryset = Medicine.objects.all().order_by("name")


class MedicineListView(LoginRequiredMixin, ListView):
    template_name = "medicines/medicine_list.html"
    queryset = Medicine.objects.all().order_by("name")


class MedicineCreateView(LoginRequiredMixin, CreateView):
    template_name = "medicines/medicine_create.html"
    model = Medicine
    success_url = reverse_lazy("medicine:medicine_list")
    form_class = medicine_forms.MedicineForm
