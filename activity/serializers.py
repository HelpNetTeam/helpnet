from rest_framework import serializers
from .models.activity import Activity
from .models.project import Project


class ActivitySerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only=True)
    # def get_likes(self, obj):
    #     return obj.likes

    comments = serializers.IntegerField(read_only=True)
    # def get_comments(self, obj):
    #     return obj.comments

    class Meta:
        model = Activity
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
