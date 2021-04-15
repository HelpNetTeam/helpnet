from django.test import TestCase
from activity.models.activity import Activity


class ActivityTestCase(TestCase):
    def setUp(self):
        Activity.objects.create(name="Activity1", latitude=0.0, longitude=0.0)
        Activity.objects.create(name="Activity2",  latitude=0.1, longitude=0.1)

    def test_activity_creation(self):
        """Activities are being properly created"""
        activity1 = Activity.objects.get(name="Activity1")
        activity2 = Activity.objects.get(name="Activity2")
        self.assertEqual(activity1.name, 'Activity1')
        self.assertEqual(activity2.name, 'Activity2')
