from rest_framework import serializers
from .models import Book, Category, Chapter


class BooksSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'sample', 'category')


class ChapterSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Chapter
        fields = ('name', 'source')


class BookSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(many=True)
    category = serializers.CharField(source='category.title')

    class Meta(object):
        model = Book
        fields = ('id', 'name', 'author', 'sample', 'category', 'chapter')
