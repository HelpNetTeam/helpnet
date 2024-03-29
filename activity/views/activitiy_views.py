from rest_framework import views
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from activity.models.activity import Activity, Comment, Review, ActivityImage
from activity.serializers import (
    ActivitySerializer, CommentSerializer, ReviewSerializer,
    ActivityLikeSerializer)


class ActivityList(APIView):

    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitySerializer(data=request.data, context={'request': request})
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
        serializer = ActivitySerializer(activity, data=request.data, context={'request': request})
        if serializer.is_valpk():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### Comment Views

class CommentActivityList(APIView):

    def get(self, request, activity):
        """Get only the comments asociated to a comment"""
        comments = Comment.objects.filter(activity=activity)
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)

class CommentCreate(APIView):
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


### Activity Likes Views

class ActivityLikeCreate(APIView):
    def post(self, request):
        serializer = ActivityLikeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityLikeDetails(APIView):

    def get_object(self, pk):
        return ActivityLike.objects.get(pk=pk)

    def get(self, request, pk):
        try: 
            activity_like = self.get_object(pk)
        except ActivityLike.DoesNotExist:
            return Response({"activity-like": "Not found."},
            status=status.HTTP_404_NOT_FOUND)

        serializer = ActivityLikeSerializer(comment, context={'request': request})
        return Response(serializer.data)
    
    def delete(self, request, pk):
        activity_like = self.get_object(pk)
        activity_like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### Review Views

class ReviewActivityList(APIView):

    def get(self, request, activity):
        """Get only the reviews associated to a review"""
        reviews = Review.objects.filter(activity=activity)
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)

class ReviewCreate(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetails(APIView):

    def get_object(self, pk):
        return Review.objects.get(pk=pk)

    def get(self, request, pk):
        try: 
            review = self.get_object(pk)
        except Review.DoesNotExist:
            return Response({"review": "Not found."},
            status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data, context={'request': request})
        if serializer.is_valpk():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

### Activity Images Views

class ActivityFileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, activity_pk, filename, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        
        f = request.data['file']

        activity = Activity.objects.get(pk=activity_pk)
        activity_image = ActivityImage.objects.create(activity=activity)

        activity_image.image.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)
