from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def book_detail(request):
    return HttpResponse("<h1>Book Details are on the way...!</h1>")


def author_details(request):
    return HttpResponse("<h1>Books author are on the way ...!</h1>")


def categories(request):
    return HttpResponse("<h1>Category of books are on the way...!</h1>")
