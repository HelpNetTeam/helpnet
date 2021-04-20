from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.profile import Profile
from core.serializers import ProfileSerializer


class ProfileList(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileCreate(APIView):

    def post(self, request):
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetails(APIView):

    def get_object(self, pk):
        return Profile.objects.get(pk=pk)

    def get(self, request, pk):
        try:
            profile = self.get_object(pk)
        except Profile.DoesNotExist:
            return Response({"profile": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
