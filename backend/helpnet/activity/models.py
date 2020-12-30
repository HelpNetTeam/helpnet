from django.db import models


class Activity(models.Model):

    name = models.CharField(max_length=100)
    project_id = models.CharField(max_length=100)  # ToDo: convert to m2o
    date = models.DateTimeField(auto_now_add=True)
    leader_id = models.CharField(max_length=100)  # ToDo: convert to m2o

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "activities"
