from django.db import models
from djchoices import ChoiceItem, DjangoChoices


# Create your models here.
class Medicine(models.Model):
    class MedicineUnits(DjangoChoices):
        mg = ChoiceItem("mg")
        ml = ChoiceItem("ml")
        tablet = ChoiceItem("tablet")
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    manufacture_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=False, blank=False)
    intake_form = models.CharField(max_length=20, choices=MedicineUnits.choices, null=False, blank=False)
    minimum_units = models.IntegerField(null=False, blank=False)
    maximum_units = models.IntegerField(null=False, blank=False)
    advisable_units = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
