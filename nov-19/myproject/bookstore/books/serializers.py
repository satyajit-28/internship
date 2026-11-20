from rest_framework import serializers
from .models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "email", "biography", "nationality"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "isbn", "price", "stock", "description", 
                  "author", "category", "category_detail"]

def validate_price(self, value):
    if value <= 0:
        raise serializers.ValidationError("Price must be grater than 0")
    return value

def validate_isbn(self, value):
    if not value.isdigit() or len(value) not in (10, 13):
        raise serializers.ValidationError("ISBN must be 10 or 13 digits (numbers only)")
    return value
