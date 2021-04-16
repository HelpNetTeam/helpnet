from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from activity.models.organization import Organization
from activity.serializers import OrganizationSerializer


class OrganizationList(APIView):

    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationDetails(APIView):

    def get_object(self, id):
        return Organization.objects.get(pk=id)

    def get(self, request, id):
        try:
            organization = self.get_object(id)
        except Organization.DoesNotExist:
            return Response({"organization": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)

    def put(self, request, id):
        organization = self.get_object(id)
        serializer = OrganizationSerializer(organization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        organization = self.get_object(id)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
