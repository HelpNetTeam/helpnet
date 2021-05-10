from django.http import response
from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse
from rest_framework import status
from core.models.profile import Profile
from activity.models.activity import Activity, Comment, Review, ActivityLike
from activity.models.category import Category
from activity.serializers import ActivitySerializer, CommentSerializer, ReviewSerializer

client = Client()
factory = RequestFactory()

class ActivityTestCase(TestCase):
    def setUp(self):
        self.user = Profile.objects.create(name="User", phone='1234567', email='u@u.com')
        self.category_a = Category.objects.create(name='Category A', description="Long description")
        self.activity1 = Activity.objects.create(
            name="Activity1",
            #date='2021-12-31 09:00:00', 
            latitude=0.0, 
            longitude=0.0,
            description='This is a long description for the activity #1',
            category=self.category_a,
            )
        self.activity2 = Activity.objects.create(
            name="Activity2",
            #date='2021-12-31 21:00:00',
            latitude=0.1,
            longitude=0.1,
            description='This is a long description for the activity #2',
            category=self.category_a,
            )

    def test_activity_creation(self):
        """Activities are being properly created"""
        self.assertEqual(self.activity1.name, 'Activity1')
        self.assertEqual(self.activity2.name, 'Activity2')

    def test_get_valid_single_activity(self):
        reversed_url = reverse('activity-detail', kwargs={'pk': self.activity1.pk})
        response = client.get(reversed_url)
        request = factory.get(reversed_url)
        serializer = ActivitySerializer(self.activity1, context={'request': request})
        self.assertEqual(response.data, serializer.data)
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
            'longitude': 0.3,
            'description': 'This is a long description for the activity #3',
        }
        response = client.post(
            path=reverse('activity-list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_activity_likes_count(self):
        """Activity likes are being computed and returned OK"""
        self.assertTrue(0 <= self.activity1.likes_count <= 100)
    
    def test_activity_comments_count(self):
        """Activity comments are being computed and returned OK"""

        data = {
            'date': '2021-12-31 09:00:00',
            'title': 'This is the first comment',
            'body': 'This is a longer message for the first comment',
            'user': self.user,
            'activity': self.activity1,
        }

        [Comment.objects.create(**data) for _ in range(5)]

        self.assertEqual(self.activity1.comments_count, 5)

    def test_comment_count_on_api_response(self):
        """Activity comments are being computed and returned OK using the API"""
        reversed_url = reverse('activity-detail', kwargs={'pk': self.activity1.pk})
        data = {
            'date': '2021-12-31 09:00:00',
            'title': 'This is the first comment',
            'body': 'This is a longer message for the first comment',
            'user': self.user,
            'activity': self.activity1,
        }

        [Comment.objects.create(**data) for _ in range(5)]

        response = client.get(reversed_url)
        request = factory.get(reversed_url)
        serializer = ActivitySerializer(self.activity1, context={'request': request})

        self.assertEqual(serializer.data.get('comments_count'), 5)

    def test_activity_likes_count(self):
        """Activity likes are being computed and returned OK"""

        data = {
            'date': '2021-12-31 09:00:00',
            'user': self.user,
            'activity': self.activity1,
        }

        [ActivityLike.objects.create(**data) for _ in range(5)]

        self.assertEqual(self.activity1.likes_count, 5)

    def test_activity_likes_count_on_api_response(self):
        """Activity likes are being computed and returned OK using the API"""
        reversed_url = reverse('activity-detail', kwargs={'pk': self.activity1.pk})
        data = {
            'date': '2021-12-31 09:00:00',
            'user': self.user,
            'activity': self.activity1,
        }

        [ActivityLike.objects.create(**data) for _ in range(5)]

        response = client.get(reversed_url)
        request = factory.get(reversed_url)
        serializer = ActivitySerializer(self.activity1, context={'request': request})

        self.assertEqual(serializer.data.get('likes_count'), 5)

    def test_category_activity_is_hyperlinked(self):
        """Activity categories are being properly hyperlinked"""
        category_reversed_url = 'http://testserver' + reverse('category-detail', kwargs={'pk': self.activity1.category.pk})
        activity_reversed_url = reverse('activity-detail', kwargs={'pk': self.activity1.pk})

        request = factory.get(activity_reversed_url)
        serializer = ActivitySerializer(self.activity1, context={'request': request})
        self.assertEqual(serializer.data.get('category'), category_reversed_url)

## Test Comments

class CommentTestCase(TestCase):
    def setUp(self):
        
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
        """Comments are being properly created"""
        self.assertEqual(self.comment1.title, 'This is the first comment')
        self.assertEqual(self.comment2.title, 'This is the second comment')

    def test_get_valid_single_comment(self):
        reversed_url = reverse('comment-detail', kwargs={'pk': self.comment1.pk})
        response = client.get(reversed_url)
        request = factory.get(reversed_url)
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
        request = factory.get(reversed_url)
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


class ActivityLikeTestCase(TestCase):

    def setUp(self):
        
        self.activity = Activity.objects.create(name="Activity1", date='2021-12-31 09:00:00', latitude=0.0, longitude=0.0)
        self.user = Profile.objects.create(name="User", phone='1234567', email='u@u.com')

        self.activity_like1 = ActivityLike.objects.create(
            date='2021-12-31 09:00:00',
            user=self.user,
            activity=self.activity,
            )
        self.activity_like2 = ActivityLike.objects.create(
            user=self.user,
            activity=self.activity,
            )
        
    def test_activity_like_creation(self):
        """Activity Likes are being properly created"""
        self.assertEqual(self.activity_like1.user, self.user)
        self.assertEqual(self.activity_like2.user, self.user)
    
    def test_activity_like_api_creation(self):
        data = {
            'user': reverse('profile-detail', kwargs={'pk': self.user.pk}),
            'activity': reverse('activity-detail', kwargs={'pk': self.activity.pk}),
        }
        response = client.post(
            path=reverse('activitylike-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)