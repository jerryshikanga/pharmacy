from rest_framework import serializers

from pharmacy.apps.medicine.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Medicine
        fields = ("name", "manufacturer", "manufacture_date", "expiry_date", "units",
                  "minimum_units", "maximum_units", "id")


class MedicineSearchSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

    def search_medicine(self):
        name = self.validated_data["name"]
        medicines = Medicine.objects.filter(name__icontains=name).order_by("name")
        return [MedicineSerializer(instance=m).data for m in medicines]

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
