import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer, BookDetailApiSerializer
from rest_framework import generics, status


# Create your views here.
def index(request):
    return HttpResponse(request, 'hello ulugbek')


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeatilApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        data = {
            'status': f'{len(serializer.data)}',
            'books': serializer.data
        }
        return Response(data)


class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        print(json.dumps(data, indent=4, ensure_ascii=False))
        serializer = BookSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': f'{len(serializer.data)}',
                'books': serializer.data

            }
            return Response(data)


class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            print('query', book)
            serializer = BookDetailApiSerializer(book).data
            print(serializer)
            data = {
                'status': 'successfully, ulugbek',
                'book': serializer
            }
            return Response(data)

        except:
            data = {
                'status': f'{status.HTTP_404_NOT_FOUND}',

            }
            return Response(data)


class DeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status': True,
                'message': 'Book deleted successfully'
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    'status': False,
                    'message': 'Book not found'

                }, status=status.HTTP_400_BAD_REQUEST
            )


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({
                'status': True,
                'message': f"Book {book_saved} updated successfully"
            })