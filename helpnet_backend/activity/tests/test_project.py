from django.test import TestCase
from activity.models.project import Project


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
