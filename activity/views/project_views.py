from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from activity.models.project import Project
from activity.serializers import ProjectSerializer


class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetails(APIView):

    def get_object(self, pk):
        return Project.objects.get(pk=pk)

    def get(self, request, pk):
        try: 
            project = self.get_object(pk)
        except Project.DoesNotExist:
            return Response({"project": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
