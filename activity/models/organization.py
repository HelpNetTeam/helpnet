from django.db import models
from core.models.profile import Profile


class Organization(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(default="No Description")
    responsible_id = models.ForeignKey(Profile, related_name='organizations', on_delete=models.SET_NULL, null=True)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name
