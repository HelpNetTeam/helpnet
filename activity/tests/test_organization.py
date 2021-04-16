from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from activity.models.organization import Organization
from activity.serializers import OrganizationSerializer

client = Client()


class OrganizationTestCase(TestCase):
    def setUp(self):
        self.organization1 = Organization.objects.create(
            name="Organization1",
            website='test1.com',
            )
        self.organization2 = Organization.objects.create(
            name="Organization2",
            website='test2.com',
            )

    def test_organization_creation(self):
        """Projects are being properly created"""
        self.assertEqual(self.organization1.name, 'Organization1')
        self.assertEqual(self.organization1.website, 'test1.com')
        self.assertEqual(self.organization2.name, 'Organization2')
        self.assertEqual(self.organization2.website, 'test2.com')

    def test_get_valid_single_organization(self):
        response = client.get(
            reverse('organization_detail', kwargs={'id': self.organization1.pk})
            )
        serializer = OrganizationSerializer(self.organization1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_organization(self):
        response = client.get(
            reverse('organization_detail', kwargs={'id': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_organization_api_creation(self):
        data = {
            'name': 'Organization3',
            'website': 'http://test3.com'
        }
        response = client.post(
            path=reverse('organization_list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)