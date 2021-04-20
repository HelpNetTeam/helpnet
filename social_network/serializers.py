from rest_framework import serializers
from .models.post import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'