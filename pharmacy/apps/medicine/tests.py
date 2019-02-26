import json

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django_dynamic_fixture import G
from django.urls import reverse

from pharmacy.apps.medicine.models import Medicine
from pharmacy.utils.test_utils import create_user, get_user_auth_token


# Create your tests here.
class MedicineTests(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.auth_token = get_user_auth_token(self.user)
        self.custom_client = APIClient()
        self.custom_client.credentials(HTTP_AUTHORIZATION="Token "+self.auth_token)

    def test_medicine_search(self):
        G(Medicine, name="Panadol")
        G(Medicine, name="Paracetamol")
        G(Medicine, name="Amoxyl")
        G(Medicine, name="Flagyl")
        G(Medicine, name="Cetrisin")
        url = reverse("medicine:medicine_search")
        data = {
            "name": "Pan"
        }
        response = self.custom_client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["name"], "Panadol")
