from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from activity.models.organization import Organization
from activity.serializers import OrganizationSerializer


class OrganizationList(APIView):

    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationDetails(APIView):

    def get_object(self, pk):
        return Organization.objects.get(pk=pk)

    def get(self, request, pk):
        try:
            organization = self.get_object(pk)
        except Organization.DoesNotExist:
            return Response({"organization": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = OrganizationSerializer(organization, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        organization = self.get_object(pk)
        serializer = OrganizationSerializer(organization, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        organization = self.get_object(pk)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
