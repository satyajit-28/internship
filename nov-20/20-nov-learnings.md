Pending

APIView
1 hr

Imagine you have a bookstore project.

You already know:

Plain Text
Browser
↓
URL
↓
View
↓
Template
↓
HTML

Example:

Python
def book_list(request):
books = Book.objects.all()
return render(request, "books.html", {"books": books})

This sends HTML to the browser.

But suppose tomorrow you need:

Android App
iOS App
React Frontend
Angular Frontend

These applications cannot use Django templates.

JSON
{
    "id": 1,
    "title": "Mrutyunjay",
    "price": 450
}

This is where APIs come in.
API is a bridge through which one software talks to another software.

What is APIView?

APIView is a class provided by Django REST Framework.

Python
from rest_framework.views import APIView

It is a special View designed for APIs.
Normal Django View:

Python
View

DRF API View:

Python
APIView

APIView understands:

JSON
HTTP methods
Authentication
Permissions
API responses

better than a normal Django View.

Purpose of APIView

APIView helps you create endpoints.

Example:

Python
/books/
/books/1/
/authors/
/authors/5/

that return JSON data.




 @api_view, Response, status codes, generic views (ListCreateAPIView, RetrieveUpdateDestroyAPIView), browsable API, request parsing.
Build: REST endpoints for books: list, create, retrieve, update, delete.
Practice: Use Postman to test all 5 operations and record results.
Deliverable: Working CRUD API with Postman collection exported to repo.