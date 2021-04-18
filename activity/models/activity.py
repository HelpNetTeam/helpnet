from random import randrange
from django.db import models

from taggit.managers import TaggableManager

from .organization import Organization
from .project import Project
from .category import Category
from .need import Need, NeedUom
from .profile import Profile

class Activity(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    responsable_id = models.ForeignKey(Profile, related_name='activities', on_delete=models.SET_NULL, null=True)
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

    def __str__(self):
        return f'{self.name} at ({self.date})'

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
    need_id = models.ForeignKey(Need, related_name='activity_needs', on_delete=models.SET_NULL, null=True)
    uom_id = models.ForeignKey(NeedUom, related_name='activity_needs', on_delete=models.SET_NULL, null=True)
    qty = models.FloatField()
    activity_id = models.ForeignKey(Activity, related_name='activity_needs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(f'{self.need_id.name}: {self.qty}')


class Comment(models.Model):

    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    body = models.TextField()
    user = models.ForeignKey(Profile, related_name='comments', on_delete=models.SET_NULL, null=True)
    # parent_id # Nested comments
    is_active = models.BooleanField(default=True)
    activity = models.ForeignKey(Activity, related_name='comments', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title[:16]

    def likes_count(self):
        pass


class CommentLike(models.Model):

    id = models.BigAutoField(primary_key=True)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='activity_comment_likes', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):

    RANKING = (
        ('1', 'Bad'),
        ('2', 'Kinda Bad'),
        ('3', 'Normal'),
        ('4', 'Great'),
        ('5', 'Excellent')
        )

    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=15, choices=RANKING)
    user = models.ForeignKey(Profile, related_name='activity_reviews', on_delete=models.SET_NULL, null=True)
    activity = models.ForeignKey(
        Activity, related_name='Reviews', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.rating
