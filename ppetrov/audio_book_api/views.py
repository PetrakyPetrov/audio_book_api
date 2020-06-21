from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Book
from .serializers import BooksSerializer, BookSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Q


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET'])
def book_list(request):
    """
        List all books.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BooksSerializer(books, many=True)
        return JSONResponse(serializer.data)


@api_view(['GET'])
def book_detail(request, pk):
    """
        Retun book detail.
    """
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return JSONResponse(serializer.data)


class Booksearch(APIView):
    """
        List all books by query params(category, author, book_name).
    """
    def get(self, request, format=None):

        serializer = {}
        book_name = None
        if 'book_name' in request.GET.keys():
            book_name = request.GET['book_name']

        author = None
        if 'author' in request.GET.keys():
            author = request.GET['author']

        category = None
        if 'category' in request.GET.keys():
            category = request.GET['category']

        books = Book.objects.filter(Q(name=book_name) | Q(author=author) | Q(category__title=category))
        serializer = BooksSerializer(books, many=True)

        return JSONResponse(serializer.data)
