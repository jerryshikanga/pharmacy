from django import forms

from pharmacy.apps.patients.models import Patient


class PatientForm(forms.ModelForm):
    class Meta(object):
        model = Patient
        fields = ("name", "date_of_birth")
