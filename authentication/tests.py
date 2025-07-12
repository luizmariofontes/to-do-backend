from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        """Ensure we can create a new user account."""
        url = reverse("create-user")  # Corrigir se necessário
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["email"], "test@example.com")
