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

    def clean_maximum_units(self):
        maximum_units = self.cleaned_data["maximum_units"]
        minimum_units = self.cleaned_data["minimum_units"]
        if minimum_units > maximum_units:
            raise ValidationError("Maximum units is less then minimum units")
        return maximum_units

    def clean_advisable_units(self):
        maximum_units = self.cleaned_data["maximum_units"]
        minimum_units = self.cleaned_data["minimum_units"]
        advisable_units = self.cleaned_data["advisable_units"]
        if advisable_units > maximum_units:
            raise ValidationError("Advisable units cannot be greater than maximum units.")
        if advisable_units < minimum_units:
            raise ValidationError("Advisable units cannot be less than minimum units.")
        return advisable_units
