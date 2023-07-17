from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from basic_app.models import Book
from basic_app.serializers1 import BookSerializer


class List(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class ListID(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class Put(APIView):
    def put(self, reqeust, pk):
        data = reqeust.data
        book = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class Post(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class Del(APIView):
    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response({'status': 'deleted'})
