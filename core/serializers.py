from rest_framework import serializers
from .models.profile import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'