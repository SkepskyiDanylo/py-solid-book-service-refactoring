from abc import ABC, abstractmethod

from app.books import Book


class Display(ABC):

    @abstractmethod
    def display(self, data: str) -> None:
        pass


class ConsoleDisplay(Display):

    def display(self, data):
        print(data)


class ReverseDisplay(Display):

    def display(self, data):
        print(data[::-1])


class BookDisplay:

    def __init__(self, display: Display):
        self.display = display

    def display_book(self, book: Book):
        self.display.display(book.content)