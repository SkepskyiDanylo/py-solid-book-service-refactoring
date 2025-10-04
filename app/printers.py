from abc import ABC, abstractmethod

from app.books import Book


class Printer(ABC):

    @abstractmethod
    def print(self, data: str) -> None:
        pass


class ConsolePrinter(Printer):

    def print(self, data: str) -> None:
        print(data)


class ReversePrinter(Printer):

    def print(self, data: str) -> None:
        print(data[::-1])


class BookPrinter:

    def __init__(self, printer: Printer) -> None:
        self.printer = printer

    def print_book(self, book: Book) -> None:
        self.printer.print(book.content)