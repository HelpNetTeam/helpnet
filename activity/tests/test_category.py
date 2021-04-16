from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from activity.models.category import Category
from activity.serializers import CategorySerializer

client = Client()


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            name="Category1",
            description='This is a description 1',
            )
        self.category2 = Category.objects.create(
            name="Category2",
            description='This is a description 2',
            )

    def test_category_creation(self):
        """Projects are being properly created"""
        self.assertEqual(self.category1.name, 'Category1')
        self.assertEqual(self.category1.description, 'This is a description 1')
        self.assertEqual(self.category2.name, 'Category2')
        self.assertEqual(self.category2.description, 'This is a description 2')

    def test_get_valid_single_category(self):
        response = client.get(
            reverse('category_detail', kwargs={'id': self.category1.pk})
            )
        serializer = CategorySerializer(self.category1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_category(self):
        response = client.get(
            reverse('category_detail', kwargs={'id': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_category_api_creation(self):
        data = {
            'name': 'Category3',
            'description': 'http://test3.com'
        }
        response = client.post(
            path=reverse('category_list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)