from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from activity.models.activity import Activity
from activity.serializers import ActivitySerializer

client = Client()

class ActivityTestCase(TestCase):
    def setUp(self):

        Activity.objects.create(name="Activity1", date='2021-12-31 09:00:00', latitude=0.0, longitude=0.0)
        Activity.objects.create(name="Activity2", date='2021-12-31 21:00:00', latitude=0.1, longitude=0.1)

    def test_activity_creation(self):
        """Activities are being properly created"""
        activity1 = Activity.objects.get(name="Activity1")
        activity2 = Activity.objects.get(name="Activity2")
        self.assertEqual(activity1.name, 'Activity1')
        self.assertEqual(activity2.name, 'Activity2')

    def test_get_valid_single_activity(self):
        activity1 = Activity.objects.get(name="Activity1")
        response = client.get(
            reverse('activity_detail', kwargs={'id': activity1.pk})
            )
        activity = Activity.objects.get(pk=activity1.pk)
        serializer = ActivitySerializer(activity)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_activity(self):
        response = client.get(
            reverse('activity_detail', kwargs={'id': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_activity_api_creation(self):
        data = {
            'name': 'Activity3',
            'date': '2021-12-31 09:00:00',
            'latitude': 0.3, 
            'longitude': 0.3
        }
        response = client.post(
            path=reverse('activity_list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_activity_likes_count(self):
        """Activity likes are being computed and returned OK"""
        activity1 = Activity.objects.get(name="Activity1")
        self.assertTrue(0 <= activity1.likes <= 100)
    
    def test_activity_comments_count(self):
        """Activity comments are being computed and returned OK"""
        activity1 = Activity.objects.get(name="Activity1")
        self.assertTrue(0 <= activity1.comments <= 100)
        # self.assertTrue(0 <= activity1.get_comments_count() <= 100)