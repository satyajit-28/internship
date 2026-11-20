Learn: Install DRF, Serializer vs ModelSerializer, APIView, @api_view, Response, status codes, generic views (ListCreateAPIView, RetrieveUpdateDestroyAPIView), browsable API, request parsing.
Build: REST endpoints for books: list, create, retrieve, update, delete.
Practice: Use Postman to test all 5 operations and record results.
Deliverable: Working CRUD API with Postman collection exported to repo.


What is DRF?
    - is a library on top of django
    - helps to build api quickly
    - Django + Django REST Framework = API Development

What is an API?
    - Suppose you have a bookstore application.
    - normal django
        Browser
           |
        Django
            |
        HTML Page
    - Request
        /books/
    - Response
        /books/
        ![alt text](image-1.png)
        Django returns HTML.
    With DRF:
        Mobile App
            |
            |
        API
            |
        DRF
            |
        Database
        Request:
            /api/books/
        Response:
                JSON
                        [
                {
                    "id": 1,
                    "title": "Rich Dad Poor Dad"
                },
                {
                    "id": 2,
                    "title": "Atomic Habits"
                }
            ]
Why Do We Need APIs?
Imagine Instagram.

You use:

Android App
iPhone App
Website

All of them need the same data.

Instead of writing separate backend code for each:

Plain Text
Android
|
iPhone
|
Website
|
API
|
Database

A single API serves all clients.

This is why APIs are used.

Why Django Alone Isn't Enough?
Django is excellent for:

Plain Text
Templates
Forms
HTML Pages
Authentication

But creating APIs manually is a lot of work.

DRF provides:

Serialization
Authentication
Permissions
Pagination
Browsable API
Validation
out of the box.

What is Serialization?
Suppose we have a model.

Python
class Book(models.Model):
title = models.CharField(max_length=100)
price = models.IntegerField()

Database object:

Python
Book(
title="Atomic Habits",
price=500
)

The mobile app cannot understand Python objects.

It understands JSON.
Serializer converts:

Python
Book Object

into:

JSON
{
"title": "Atomic Habits",
"price": 500
}
This process is called:

Plain Text
Serialization

Main Components of DRF
1. Model
Python
class Book(models.Model):
title = models.CharField(max_length=100)

Stores data.

2. Serializer
Python
class BookSerializer(serializers.ModelSerializer):
class Meta:
model = Book
fields = "__all__"

Converts:

Plain Text
Python Object
↔
JSON
3. View

Handles request and response.

Python
class BookList(APIView):
pass
4. URL
Python
path("api/books/", BookList.as_view())

Connects URL to View.

Serializer vs modelserializer
Why Do We Need a Serializer?
Suppose you have a model:

Python
class Book(models.Model):
title = models.CharField(max_length=100)
price = models.IntegerField()

And data in the database:

Plain Text
Book:
title = "Atomic Habits"
price = 500
 

Python understands this as a Book object.

But a mobile app or React frontend cannot understand Python objects.

They understand:

JSON
{
"title": "Atomic Habits",
"price": 500
}

So DRF needs someone to convert:

Plain Text
Python Object
↕
JSON

That someone is called a Serializer.

What is Serializer?

Serializer is a class where you manually define every field.
Example:

Python
from rest_framework import serializers
 
class BookSerializer(serializers.Serializer):
title = serializers.CharField(max_length=100)
price = serializers.IntegerField()

Now DRF knows:

Plain Text
title → string
price → integer

Why Was Serializer Created?

Imagine you are not using Django models.

Maybe your data comes from:

External API
Excel File
CSV
Dictionary
Custom Python Class

Example:

Python
student = {
"name": "Rahul",
"age": 25
}

No model exists.

Still, you need validation.

Serializer solves this problem.

Problem With Serializer

Suppose model:

Python
class Book(models.Model):
title = models.CharField(max_length=100)
price = models.IntegerField()
author = models.CharField(max_length=50)
isbn = models.CharField(max_length=20)

Now in Serializer:

Python
class BookSerializer(serializers.Serializer):
title = serializers.CharField()
price = serializers.IntegerField()
author = serializers.CharField()
isbn = serializers.CharField()

Notice something?

You're writing fields twice.

Plain Text
Model
+
Serializer

Duplicate work.