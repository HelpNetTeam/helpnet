from rest_framework import serializers
from core.models.profile import Profile
from .models.activity import Activity, Comment, Review, ActivityLike
from .models.project import Project
from .models.organization import Organization
from .models.category import Category
from .models.need import Need, NeedUom


class ActivitySerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    category = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='category-detail'
    )
    project = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='project-detail'
    )
    organization = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='organization-detail'
    )
    responsible = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='profile-detail'
    )

    class Meta:
        model = Activity
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class ActivityLikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ActivityLike
        fields = '__all__'

class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = '__all__'

class NeedUomSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedUom
        fields = '__all__'
