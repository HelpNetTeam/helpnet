from django.db import models
from core.models.profile import Profile
from .organization import Organization


class Project(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(default="No Description")
    organization_id = models.ForeignKey(Organization, related_name='projects', on_delete=models.SET_NULL, null=True)
    responsible_id = models.ForeignKey(Profile, related_name='projects', on_delete=models.SET_NULL, null=True)
    website = models.URLField()

    def __str__(self):
        return self.name
