from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pharmacy.apps.medicine.models import Medicine
from pharmacy.apps.patients.models import Patient


@login_required
def index(request, *args, **kwargs):
    context = {
        'patients': Patient.objects.all().order_by("name"),
        'medicines': Medicine.objects.all().order_by("name")
    }
    return render(request, "index.html", context=context)
