from django.db import models
from core.models.profile import Profile


class Post(models.Model):
    
    title = models.CharField(max_length=200)
    user = models.ForeignKey(Profile, related_name='posts', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    share_count = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    
    # @property
    # def likes_count(self):
    #     return self.likes.count()

# class Likes:


# class Comments