from decimal import Decimal

from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'genre', 'isbn',
                  'price', 'discount_price', 'author']

    discount_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book: Book):
        return book.price * Decimal(0.1)
