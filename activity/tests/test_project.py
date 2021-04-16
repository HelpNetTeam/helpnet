from django.conf.urls import url
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from activity.models.project import Project
from activity.serializers import ProjectSerializer

client = Client()

class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(name="Project1", website='test1.com')
        Project.objects.create(name="Project2",  website='test2.com')

    def test_project_creation(self):
        """Projects are being properly created"""
        project1 = Project.objects.get(name="Project1")
        project2 = Project.objects.get(name="Project2")
        self.assertEqual(project1.name, 'Project1')
        self.assertEqual(project1.website, 'test1.com')
        self.assertEqual(project2.name, 'Project2')
        self.assertEqual(project2.website, 'test2.com')

    def test_get_valid_single_project(self):
        project1 = Project.objects.get(name="Project1")
        response = client.get(
            reverse('project_detail', kwargs={'id': project1.pk})
            )
        project = Project.objects.get(pk=project1.pk)
        serializer = ProjectSerializer(project)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_project(self):
        response = client.get(
            reverse('project_detail', kwargs={'id': 30})
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_project_api_creation(self):
        data = {
            'name': 'Project3',
            'website': 'http://test3.com'
        }
        response = client.post(
            path=reverse('project_list'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)