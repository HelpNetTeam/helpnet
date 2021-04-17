from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from activity.models.need import Need, NeedUom
from activity.serializers import NeedSerializer, NeedUomSerializer


class NeedList(APIView):

    def get(self, request):
        needs = Need.objects.all()
        serializer = NeedSerializer(needs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NeedDetails(APIView):

    def get_object(self, id):
        return Need.objects.get(pk=id)

    def get(self, request, id):
        try:
            need = self.get_object(id)
        except Need.DoesNotExist:
            return Response({"need": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = NeedSerializer(need)
        return Response(serializer.data)

    def put(self, request, id):
        need = self.get_object(id)
        serializer = NeedSerializer(need, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        need = self.get_object(id)
        need.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### Need Uom Views

class NeedUomList(APIView):

    def get(self, request):
        need_uoms = NeedUom.objects.all()
        serializer = NeedUomSerializer(need_uoms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NeedUomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NeedUomDetails(APIView):

    def get_object(self, id):
        return NeedUom.objects.get(pk=id)

    def get(self, request, id):
        try:
            need_uom = self.get_object(id)
        except NeedUom.DoesNotExist:
            return Response({"need_uom": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = NeedUomSerializer(need_uom)
        return Response(serializer.data)

    def put(self, request, id):
        need_uom = self.get_object(id)
        serializer = NeedUomSerializer(need_uom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        need_uom = self.get_object(id)
        need_uom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
