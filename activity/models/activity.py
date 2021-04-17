from random import randrange
from django.db import models

from taggit.managers import TaggableManager

from .organization import Organization
from .project import Project
from .category import Category
from .need import Need, NeedUom


class Activity(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # responsable_id = models.ForeignKey(User, related_name='activities', on_delete=models.SET_NULL)
    organization_id = models.ForeignKey(Organization, related_name='activities', on_delete=models.SET_NULL, null=True)
    project_id = models.ForeignKey(Project, related_name='activities', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True)
    address = models.TextField(null=True)
    country_id = models.IntegerField(null=True)
    state_id = models.IntegerField(null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    category_id = models.ForeignKey(Category, related_name="activities", on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()

    # def __str__(self):
    #     return self.name + ''

    class Meta:
        verbose_name_plural = "activities"

    @property
    def likes_count(self):
        return randrange(100)

    @property
    def comments_count(self):
        return randrange(100)

    # class Meta:
    #     ordering = ['-likes','-comments']


class NeedActivity(models.Model):

    id = models.BigAutoField(primary_key=True)
    need_id = models.ForeignKey(Need, related_name='needs', on_delete=models.SET_NULL, null=True)
    uom_id = models.ForeignKey(NeedUom, related_name='uoms', on_delete=models.SET_NULL, null=True)
    qty = models.FloatField()
    activity_id = models.ForeignKey(Activity, related_name='%(class)s_activities', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(f'{self.need_id.name}: {self.qty}')


class Comment(models.Model):

    id = models.BigAutoField(primary_key=True)
    comment = models.TextField()
    # user_id = models.Many2one('res.partner')
    activity_id = models.ForeignKey(Activity, related_name='comments', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment[:16]


class Rating(models.Model):

    ranking = (
        ('1', 'Bad'),
        ('2', 'Kinda Bad'),
        ('3', 'Normal'),
        ('4', 'Great'),
        ('5', 'Excellent')
        )

    id = models.BigAutoField(primary_key=True)
    rating = models.CharField(max_length=15, choices=ranking)
    # user_id = models.Many2one('res.partner')
    activity_id = models.ForeignKey(Activity, related_name='%(class)s_activities', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.rating
