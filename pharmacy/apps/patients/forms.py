from django import forms

from pharmacy.apps.patients.models import Patient


class PatientForm(forms.ModelForm):
    date_of_birth = forms.DateField(help_text="Format YYYY - MM - DD")

    class Meta(object):
        model = Patient
        fields = ("name", "date_of_birth")
