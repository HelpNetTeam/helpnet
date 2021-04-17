from rest_framework import serializers
from .models.activity import Activity
from .models.project import Project
from .models.organization import Organization
from .models.category import Category
from .models.need import Need, NeedUom


class ActivitySerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
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