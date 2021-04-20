from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse
from rest_framework import status
from core.models.profile import Profile
from core.serializers import ProfileSerializer

client = Client()


class ProfileTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.profile1 = Profile.objects.create(
            name="Profile1",
            phone='1234567',
            email='p@p.com',
            )
        self.profile2 = Profile.objects.create(
            name="Profile2",
            phone='1234562',
            email='p2@p.com',
            )

    def test_profile_creation(self):
        """Projects are being properly created"""
        self.assertEqual(self.profile1.name, 'Profile1')
        self.assertEqual(self.profile1.email, 'p@p.com')
        self.assertEqual(self.profile2.name, 'Profile2')
        self.assertEqual(self.profile2.email, 'p2@p.com')

    def test_get_valid_single_profile(self):
        reversed_url = reverse('profile-detail', kwargs={'pk': self.profile1.pk})

        response = client.get(reversed_url)
        request = self.factory.get(reversed_url)
        serializer = ProfileSerializer(self.profile1, context={'request': request})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_profile(self):
        response = client.get(
            reverse('profile-detail', kwargs={'pk': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_profile_api_creation(self):
        data = {
            'name': 'Profile3',
            'description': 'http://test3.com'
        }
        response = client.post(
            path=reverse('profile-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)