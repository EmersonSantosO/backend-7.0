from django.db import models


class Book:
    def __init__(self, title, isbn, year):
        self.title = title
        self.isbn = isbn
        self.year = year


class Library:
    def __init__(self):
        b1 = Book("El señor de los anillos", "01", 1954)
        b2 = Book("El hobbit", "02", 1937)
        self.books = [b1, b2]

    def add_book(self, book):
        if isinstance(book, Book):
            if book.isbn == "" or book.title == "" or book.year == "":
                return "missing data"
            else:
                for b in self.books:
                    if b.isbn == book.isbn:
                        return "book already exists"
                self.books.append(book)
                return "book added"
        else:
            return "missing data"

    def list_books(self):
        return self.books

    def delete_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                try:
                    self.books.remove(b)
                    return "book deleted"
                except:
                    return "book not found"
        return "book not found"
