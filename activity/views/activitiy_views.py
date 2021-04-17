from rest_framework import views
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from activity.models.activity import Activity, Comment
from activity.serializers import ActivitySerializer, CommentSerializer


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


# class ActivityView(viewsets.ModelViewSet):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer


class ActivityDetails(APIView):

    def get_object(self, pk):
        return Activity.objects.get(pk=pk)

    def get(self, request, pk):
        try: 
            activity = self.get_object(pk)
        except Activity.DoesNotExist:
            return Response({"activity": "Not found."},
            status=status.HTTP_404_NOT_FOUND)

        serializer = ActivitySerializer(activity, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valpk():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### Comment Views

class CommentList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetails(APIView):

    def get_object(self, pk):
        return Comment.objects.get(pk=pk)

    def get(self, request, pk):
        try: 
            comment = self.get_object(pk)
        except Comment.DoesNotExist:
            return Response({"comment": "Not found."},
            status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data, context={'request': request})
        if serializer.is_valpk():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)