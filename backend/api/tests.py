from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import LabTest


User = get_user_model()


class LabTestSecurityTests(APITestCase):

    def setUp(self):
        self.technician = User.objects.create_user(
            username="technician_test",
            password="StrongPassword123!",
            role="TECHNICIAN",
        )

        self.patient = User.objects.create_user(
            username="patient_test",
            password="StrongPassword123!",
            role="PATIENT",
        )

        self.url = "/api/tests/"

        LabTest.objects.create(
            name="CBC",
            description="Complete Blood Count",
            price=500,
            is_active=True,
        )

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_without_token_is_rejected(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 401)

    def test_technician_can_access_tests(self):
        token = self.get_token(self.technician)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_patient_cannot_access_tests(self):
        token = self.get_token(self.patient)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)

    def test_fake_token_is_rejected(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer fake.invalid.token"
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 401)