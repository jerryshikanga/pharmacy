from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import permissions as drf_permissions

from pharmacy.apps.medicine import serializers
from pharmacy.apps.medicine.models import Medicine


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
