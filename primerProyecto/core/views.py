from django.shortcuts import render
from core.models import Book, Library

l = Library()


def home(request):
    return render(request, "home.html")


def book_list(request):
    context = {"context": l.books}  # changed 'books_list' to 'books'
    return render(request, "book_list.html", context)


def book_register(request):
    return render(request, "book_register.html")


def book_created(request):
    title = request.POST.get("title")
    isbn = request.POST.get("isbn")
    year = request.POST.get("year")
    b = Book(title, isbn, year)
    response = l.add_book(b)
    context = {"context": response}
    return render(request, "book_created.html", context)


def book_deleted(request):
    isbn = request.POST.get("isbn")
    response = l.delete_book(isbn)
    context = {"context": response}
    return render(request, "book_deleted.html", context)
