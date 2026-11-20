# Django REST Framework (DRF) --- APIView and REST APIs

**Status:** Pending\
**Estimated time:** 1 hour\
**Project:** Bookstore

------------------------------------------------------------------------

## 1. Understanding the Need for APIs

In a traditional Django application, a request usually follows this
flow:

``` text
Browser
   ↓
URL
   ↓
View
   ↓
Template
   ↓
HTML response
```

For example:

``` python
def book_list(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})
```

This view retrieves all books and sends the data to a Django template,
which generates HTML for the browser.

However, suppose the same bookstore data must also be accessed by an
Android app, an iOS app, a React frontend, or an Angular frontend. These
applications may not use Django templates.

Instead, they can communicate with the Django backend through an **API
(Application Programming Interface)**.

An API acts as a bridge that allows different software applications to
communicate and exchange data.

For example, an API can return book details in JSON format:

``` json
{
    "id": 1,
    "title": "Mrutyunjay",
    "price": 450
}
```

The client application can read this JSON data and display it in its own
interface.

## 2. What Is an APIView?

`APIView` is a class-based view provided by Django REST Framework (DRF).

``` python
from rest_framework.views import APIView
```

It is designed specifically for building API endpoints. Unlike a
traditional Django view, an `APIView` provides built-in support for REST
framework features such as:

-   Handling HTTP methods such as `GET`, `POST`, `PUT`, `PATCH`, and
    `DELETE`.
-   Parsing incoming request data, including JSON.
-   Returning API responses through DRF's `Response` class.
-   Authentication and permission handling.
-   Configurable response rendering, including JSON and the browsable
    API.

### Django View vs. DRF APIView

  -----------------------------------------------------------------------
  Django View                         DRF APIView
  ----------------------------------- -----------------------------------
  Commonly used to return HTML        Designed to build API endpoints.
  responses through templates.        

  Uses Django's `HttpRequest` and     Uses DRF's enhanced `Request` and
  `HttpResponse`.                     `Response`.

  Requires additional handling for    Integrates with DRF features such
  some API features.                  as authentication, permissions, and
                                      request parsing.
  -----------------------------------------------------------------------

## 3. Purpose of APIView

`APIView` helps create API endpoints that expose application data and
operations.

Examples of bookstore endpoints:

``` text
/books/       → List all books or create a book
/books/1/     → Retrieve, update, or delete a particular book
/authors/     → List authors or create an author
/authors/5/   → Access or modify a particular author
```

These endpoints allow different client applications to interact with the
bookstore backend using HTTP requests and JSON data.

------------------------------------------------------------------------

## 4. Topics to Learn

1.  `APIView` and its purpose.
2.  The `@api_view` decorator for creating function-based API views.
3.  DRF's `Response` class.
4.  HTTP status codes and the `status` module.
5.  Generic views:
    -   `ListCreateAPIView`
    -   `RetrieveUpdateDestroyAPIView`
6.  Browsable API and how to explore API endpoints through a browser.
7.  Request parsing and handling incoming data.

## 5. Practical Implementation --- Bookstore CRUD API

Build REST API endpoints for the `Book` model to support all five CRUD
operations:

  Operation   HTTP method       Purpose
  ----------- ----------------- ---------------------------------------
  List        `GET`             Retrieve all books.
  Create      `POST`            Add a new book.
  Retrieve    `GET`             Retrieve a particular book by its ID.
  Update      `PUT` / `PATCH`   Update an existing book.
  Delete      `DELETE`          Delete a book.

### Suggested endpoints

``` text
GET     /books/       List all books
POST    /books/       Create a book
GET     /books/1/     Retrieve book with ID 1
PUT     /books/1/     Update book with ID 1
PATCH   /books/1/     Partially update book with ID 1
DELETE  /books/1/     Delete book with ID 1
```

## 6. Practice and Deliverables

**Practice:** - Use Postman to test all five CRUD operations. - Verify
the request data, response body, and HTTP status codes. - Record the
results of each operation.

**Deliverable:** - A working CRUD API for the bookstore. - An exported
Postman collection committed to the project repository.

------------------------------------------------------------------------

## Quick Revision

-   **API:** A way for software applications to communicate and exchange
    data.
-   **JSON:** A commonly used format for exchanging structured data.
-   **APIView:** A DRF class-based view designed for building APIs.
-   **Response:** DRF class used to return API responses.
-   **CRUD:** Create, Read, Update, and Delete.
-   **Postman:** A tool used to send API requests and test responses.


 @api_view, Response, status codes, generic views (ListCreateAPIView, RetrieveUpdateDestroyAPIView), browsable API, request parsing.
Build: REST endpoints for books: list, create, retrieve, update, delete.
Practice: Use Postman to test all 5 operations and record results.
Deliverable: Working CRUD API with Postman collection exported to repo.