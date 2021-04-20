from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from social_network.models.post import Post
from social_network.serializers import PostSerializer

class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetails(APIView):

    def get_object(self, pk):
        return Post.objects.get(pk=pk)

    def get(self, request, pk):
        try:
            post = self.get_object(pk)
        except Post.DoesNotExist:
            return Response({"post": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valpk():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
