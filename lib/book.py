#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_open = False  # A simple attribute to track whether the book is open or closed

    def open(self):
        self.is_open = True
        print(f"The book '{self.title}' is now open.")

    def close(self):
        self.is_open = False
        print(f"The book '{self.title}' is now closed.")

    def read(self, page):
        if self.is_open:
            print(f"Reading page {page} of '{self.title}'.")
        else:
            print(f"Please open the book '{self.title}' to read.")
        