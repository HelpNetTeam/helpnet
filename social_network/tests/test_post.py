from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse
from rest_framework import status
from core.models.profile import Profile
from social_network.models.post import Post
from social_network.serializers import PostSerializer

client = Client()
factory = RequestFactory()


class PostTestCase(TestCase):
    def setUp(self):
        self.user = Profile.objects.create(name="User", phone='1234567', email='u@u.com')
        self.post1 = Post.objects.create(
            title="Post1",
            body='This is the Post body',
            user=self.user,
        )
        self.post2 = Post.objects.create(
            title="Post2",
            body='This is the Post body',
            user=self.user,
        )

    def test_post_creation(self):
        """Projects are being properly created"""
        self.assertEqual(self.post1.title, 'Post1')
        self.assertEqual(self.post1.body, 'This is the Post body')
        self.assertEqual(self.post2.title, 'Post2')
        self.assertEqual(self.post2.body, 'This is the Post body')

    def test_get_valid_single_post(self):
        reversed_url = reverse('post-detail', kwargs={'pk': self.post1.pk})
        
        response = client.get(reversed_url)
        request = factory.get(reversed_url)
        serializer = PostSerializer(self.post1, context={'request': request})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_post(self):
        response = client.get(
            reverse('post-detail', kwargs={'pk': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_api_creation(self):
        data = {
            'title': 'Post3',
            'body': 'This is the Post body',
            'user': reverse('profile-detail', kwargs={'pk': self.user.pk}),
        }
        response = client.post(
            path=reverse('post-list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
