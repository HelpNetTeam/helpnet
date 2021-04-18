from django.http import response
from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse
from rest_framework import status
from activity.models.activity import Activity, Comment, Review
from activity.serializers import ActivitySerializer, CommentSerializer, ReviewSerializer
from activity.models.profile import Profile

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
            reverse('activity-detail', kwargs={'pk': activity1.pk})
            )
        activity = Activity.objects.get(pk=activity1.pk)
        serializer = ActivitySerializer(activity)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_activity(self):
        response = client.get(
            reverse('activity-detail', kwargs={'pk': 30})
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
            path=reverse('activity-list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_activity_likes_count(self):
        """Activity likes are being computed and returned OK"""
        activity1 = Activity.objects.get(name="Activity1")
        self.assertTrue(0 <= activity1.likes_count <= 100)
    
    def test_activity_comments_count(self):
        """Activity comments are being computed and returned OK"""
        activity1 = Activity.objects.get(name="Activity1")
        self.assertTrue(0 <= activity1.comments_count <= 100)
        # self.assertTrue(0 <= activity1.get_comments_count() <= 100)

## Test Comments

class CommentTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        self.activity = Activity.objects.create(name="Activity1", date='2021-12-31 09:00:00', latitude=0.0, longitude=0.0)
        self.user = Profile.objects.create(name="User", phone='1234567', email='u@u.com')

        self.comment1 = Comment.objects.create(
            date='2021-12-31 09:00:00',
            title="This is the first comment",
            body='This is a longer message for the first comment',
            user=self.user,
            activity=self.activity,
            )
        self.comment2 = Comment.objects.create(
            date='2022-12-31 09:00:00',
            title="This is the second comment",
            body='This is a longer message for the second comment',
            user=self.user,
            activity=self.activity,
            )

    def test_comment_creation(self):
        """Activities are being properly created"""
        comment1 = Comment.objects.get(title="This is the first comment")
        comment2 = Comment.objects.get(title="This is the second comment")
        self.assertEqual(comment1.title, 'This is the first comment')
        self.assertEqual(comment2.title, 'This is the second comment')

    def test_get_valid_single_comment(self):
        response = client.get(
            reverse('comment-detail', kwargs={'pk': self.comment1.pk})
            )
        request = self.factory.get(
            reverse('comment-detail', kwargs={'pk': self.comment1.pk})
            )
        serializer = CommentSerializer(self.comment1, context={'request': request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_comment(self):
        response = client.get(
            reverse('comment-detail', kwargs={'pk': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_comment_api_creation(self):
        data = {
            'date': '2022-12-31 03:00:00',
            'title': "This is the third comment",
            'body': 'This is a longer message for the third comment',
            'user': reverse('profile-detail', kwargs={'pk': self.user.pk}),
            'activity': reverse('activity-detail', kwargs={'pk': self.activity.pk}),
        }
        response = client.post(
            path=reverse('comment-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

## Test Reviews

class ReviewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.activity = Activity.objects.create(name="Activity1", date='2021-12-31 09:00:00', latitude=0.0, longitude=0.0)
        self.user = Profile.objects.create(name="User", phone='1234567', email='u@u.com')

        self.review1 = Review.objects.create(
            rating='5',
            user=self.user,
            activity=self.activity,
            )
        self.review2 = Review.objects.create(
            rating='4',
            user=self.user,
            activity=self.activity,
            )

    def test_review_creation(self):
        """Reviews are being properly created"""
        self.assertEqual(self.review1.rating, '5')
        self.assertEqual(self.review2.rating, '4')

    def test_get_valid_single_review(self):
        reversed_url = reverse('review-detail', kwargs={'pk': self.review1.pk})

        response = client.get(reversed_url)
        request = self.factory.get(reversed_url)
        serializer = ReviewSerializer(self.review1, context={'request': request})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_review(self):
        response = client.get(
            reverse('review-detail', kwargs={'pk': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_review_api_creation(self):
        data = {
            'rating': '4',
            'user': reverse('profile-detail', kwargs={'pk': self.user.pk}),
            'activity': reverse('activity-detail', kwargs={'pk': self.activity.pk}),
        }
        response = client.post(
            path=reverse('review-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
