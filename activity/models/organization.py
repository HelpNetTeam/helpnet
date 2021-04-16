from django.db import models


class Organization(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    responsible_id = models.IntegerField(null=True)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name
