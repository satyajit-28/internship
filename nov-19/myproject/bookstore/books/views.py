from django.shortcuts import render
from rest_framework import filters, viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author", "category").order_by("-id")
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "isbn", "author__name", "category__name"]
    ordering_fields = ["title", "price", "stock"]