from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from activity.models.need import Need, NeedUom
from activity.serializers import NeedSerializer, NeedUomSerializer

client = Client()


class NeedTestCase(TestCase):
    def setUp(self):
        self.need1 = Need.objects.create(
            name="Food",
            description='Food Need description',
            )
        self.need2 = Need.objects.create(
            name="Drink",
            description='Drink Need description',
            )

    def test_need_creation(self):
        """Needs are being properly created"""
        self.assertEqual(self.need1.name, 'Food')
        self.assertEqual(self.need1.description, 'Food Need description')
        self.assertEqual(self.need2.name, 'Drink')
        self.assertEqual(self.need2.description, 'Drink Need description')

    def test_get_valid_single_need(self):
        response = client.get(
            reverse('need_detail', kwargs={'id': self.need1.pk})
            )
        serializer = NeedSerializer(self.need1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_need(self):
        response = client.get(
            reverse('need_detail', kwargs={'id': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_need_api_creation(self):
        data = {
            'name': 'Need3',
            'description': 'need 3'
        }
        response = client.post(
            path=reverse('need_list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


### Need UoM Tests


class NeedUomTestCase(TestCase):
    def setUp(self):
        self.need_uom1 = NeedUom.objects.create(
            name="Kg",
            description='Kg description',
            )
        self.need_uom2 = NeedUom.objects.create(
            name="Lts",
            description='Lts description',
            )

    def test_need_uom_creation(self):
        """Need Uoms are being properly created"""
        self.assertEqual(self.need_uom1.name, 'Kg')
        self.assertEqual(self.need_uom1.description, 'Kg description')
        self.assertEqual(self.need_uom2.name, 'Lts')
        self.assertEqual(self.need_uom2.description, 'Lts description')

    def test_get_valid_single_need_uom(self):
        response = client.get(
            reverse('need_uom_detail', kwargs={'id': self.need_uom1.pk})
            )
        serializer = NeedUomSerializer(self.need_uom1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_need_uom(self):
        response = client.get(
            reverse('need_uom_detail', kwargs={'id': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_need_uom_api_creation(self):
        data = {
            'name': 'NeedUom3',
            'description': 'need uom 3'
        }
        response = client.post(
            path=reverse('need_uom_list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)