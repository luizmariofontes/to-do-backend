from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import uuid

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        """Ensure we can create a new user account with unique credentials."""
        unique_id = str(uuid.uuid4())
        username = f"testuser_{unique_id[:8]}"
        email = f"test_{unique_id[:8]}@example.com"

        url = reverse("create-user")
        data = {
            "username": username,
            "email": email,
            "password": "testpassword123"
        }
        response = self.client.post(url, data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], username)
        self.assertEqual(response.data["email"], email)
