from django import forms
from pharmacy.apps.medicine.models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta(object):
        model = Medicine
