from random import randrange
from django.db import models

from taggit.managers import TaggableManager

from core.models.profile import Profile
from .organization import Organization
from .project import Project
from .category import Category
from .need import Need, NeedUom

class Activity(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    responsible = models.ForeignKey(Profile, related_name='activities', on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, related_name='activities', on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, related_name='activities', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True)
    address = models.TextField(null=True)
    country_id = models.IntegerField(null=True)
    state_id = models.IntegerField(null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name="activities", on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()

    def __str__(self):
        return f'{self.name} at ({self.date})'

    class Meta:
        verbose_name_plural = "activities"

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()

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

class ActivityLike(models.Model):

    id = models.BigAutoField(primary_key=True)
    activity = models.ForeignKey(Activity, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='activity_likes', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model): # TODO: This should be called CommentActivity

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


class CommentLike(models.Model): # TODO: This should be called CommentActivityLikes

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
