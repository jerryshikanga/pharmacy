from django import forms
from django.core.validators import ValidationError

from pharmacy.apps.prescriptions.models import Prescription


class PrescriptionForm(forms.ModelForm):
    class Meta(object):
        model = Prescription
        fields = ("medicine", "patient", "additional_comments", "units")

    def clean_units(self):
        medicine = self.cleaned_data["medicine"]
        units = self.cleaned_data["units"]
        if units > medicine.maximum_units:
            raise ValidationError("{} {} is more than the recommended {} {}.".format(
                units, medicine.intake_form, medicine.maximum_units, medicine.intake_form))
        if units < medicine.minimum_units:
            raise ValidationError("{} {} is less than the recommended {} {}.".format(
                units, medicine.intake_form, medicine.minimum_units, medicine.intake_form))
        return units
