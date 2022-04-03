from django.urls import path
from .views import books_list, book_detail, book_create

urlpatterns = [
    path("", books_list, name="books-list"),
    path("books/<int:pk>", book_detail, name="book-detail"),
    path("books/create/", book_create, name="book-create"),
]




