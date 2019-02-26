from rest_framework import serializers

from pharmacy.apps.patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Patient
        fields = ("name", "date_of_birth", "id")
