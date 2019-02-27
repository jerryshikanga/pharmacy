from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

from pharmacy.apps.medicine.models import Medicine
from pharmacy.apps.patients.models import Patient


# Create your models here.
class Prescription(TimeStampedModel):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=False, blank=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False, blank=False)
    units = models.IntegerField(null=False, blank=False)
    additional_comments = models.TextField(null=True, blank=True)
    prescriber = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} of {} prescribed to {}.".format(self.units, self.medicine.intake_form, self.medicine.name, self.patient.name)
