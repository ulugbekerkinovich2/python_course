from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from second_app.models import University
from second_app.serializers import UniversitySerializer


# Create your views here.
class ListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = University.objects.all()
        serializer = UniversitySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = UniversitySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, pk):
    #     data = get_object_or_404(University, id=pk)
    #     serializer = UniversitySerializer(data).data
    #     return Response(serializer)

    # def put(self, request, pk):
    #     data_ = request.data
    #     data = get_object_or_404(University, id=pk)
    #     serializer = UniversitySerializer(data, data_)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     try:
    #         data = University.objects.get(id=pk)
    #         data.delete()
    #         return Response({'message': f'object id={pk} deleted'}, status=status.HTTP_200_OK)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
