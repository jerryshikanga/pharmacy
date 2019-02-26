from django.db import models


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name
