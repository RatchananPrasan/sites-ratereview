from rest_framework import serializers
from .models import Book, Author, BookRating

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        book = Book
        author = Author
        bookRating = BookRating
        fields = '__all__'
    