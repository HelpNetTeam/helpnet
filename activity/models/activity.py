from random import randrange
from django.db import models

from taggit.managers import TaggableManager


class Activity(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # organization_id = models.Many2one('helpnet.organization')
    # project_id = models.Many2one('helpnet.project')
    date = models.DateTimeField()
    address = models.TextField(null=True)
    country_id = models.IntegerField(null=True)
    state_id = models.IntegerField(null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    # category_id = models.Many2one('helpnet.category', 'Category')
    # need_ids = models.One2many('helpnet.activity.need', 'activity_id')
    tags = TaggableManager()
    # comment_ids = models.One2many('helpnet.activity.comment', 'activity_id')
    # rating_ids = models.One2many('helpnet.activity.rating', 'activity_id')

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



class ActivityNeed(models.Model):

    id = models.BigAutoField(primary_key=True)
    # need_id = models.Many2one('helpnet.need')
    # uom_id = models.Many2one('helpnet.need.uom')
    amount = models.FloatField()
    # activity_id = models.Many2one('helpnet.activity')

    def __str__(self):
        return str(self.amount)


class ActivityComment(models.Model):

    id = models.BigAutoField(primary_key=True)
    comment = models.TextField()
    # partner_id = models.Many2one('res.partner')
    # activity_id = models.Many2one('helpnet.activity')

    def __str__(self):
        return self.comment[:16]


class ActivityRating(models.Model):

    ranking = (
        ('1', 'Bad'),
        ('2', 'Kinda Bad'),
        ('3', 'Normal'),
        ('4', 'Great'),
        ('5', 'Excellent')
        )

    id = models.BigAutoField(primary_key=True)
    rating = models.CharField(max_length=15, choices=ranking)
    # partner_id = models.Many2one('res.partner')
    # activity_id = models.Many2one('helpnet.activity')

    def __str__(self):
        return self.rating
