from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Activity
from .serializers import ActivitySerializer


class ActivityList(APIView):

    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityDetails(APIView):

    def get_object(self, id):
        try:
            return Activity.objects.get(pk=id)
        except Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    def put(self, request, id):
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        activity = self.get_object(id)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
