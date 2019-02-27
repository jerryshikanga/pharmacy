from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pharmacy.apps.medicine.models import Medicine
from pharmacy.apps.patients.models import Patient
from pharmacy.apps.profiles.models import Account
from pharmacy.apps.prescriptions.models import Prescription


@login_required
def index(request, *args, **kwargs):
    context = {
        'patients': Patient.objects.all().order_by("name"),
        'medicines': Medicine.objects.all().order_by("name"),
        "prescriptions": Prescription.objects.all().order_by("-id"),
        "accounts": Account.objects.all().order_by("user__username")
    }
    return render(request, "index.html", context=context)
