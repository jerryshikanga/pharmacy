from django import forms
from django.utils import timezone
from django.core.validators import ValidationError
from pharmacy.apps.medicine.models import Medicine


class MedicineForm(forms.ModelForm):
    manufacture_date = forms.DateField(help_text="Format YYYY - MM - DD")
    expiry_date = forms.DateField(help_text="Format YYYY - MM - DD")

    class Meta(object):
        model = Medicine
        fields = ("name", "manufacturer", "manufacture_date", "expiry_date", "intake_form",
                  "minimum_units", "maximum_units", "advisable_units")

    def clean_manufacture_date(self):
        manufacture_date = self.cleaned_data["manufacture_date"]
        if timezone.now().date() <= manufacture_date:
            raise ValidationError("Date of Manufacture cannot be later than current date.")
        return manufacture_date

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data["expiry_date"]
        if expiry_date <= timezone.now().date():
            raise ValidationError("Product cannot be already expired.")
        return expiry_date
