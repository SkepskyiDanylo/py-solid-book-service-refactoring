import json

from app.displayers import ConsoleDisplay, ReverseDisplay, BookDisplay
from app.printers import ConsolePrinter, ReversePrinter, BookPrinter
from app.serializers import JsonSerializer, XmlSerializer, BookSerializer


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str | list[str]:
    serializing_results = []

    for cmd, method_type in commands:
        if cmd == "display":

            if method_type == "console":
                display = ConsoleDisplay()
            elif method_type == "reverse":
                display = ReverseDisplay()
            else:
                raise ValueError(f"Unknown method type: {method_type}")
            BookDisplay(display).display_book(book)

        elif cmd == "print":
            if method_type == "console":
                printer = ConsolePrinter()
            elif method_type == "reverse":
                printer = ReversePrinter()
            else:
                raise ValueError(f"Unknown method type: {method_type}")
            BookPrinter(printer).print_book(book)

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer()
            elif method_type == "xml":
                serializer = XmlSerializer()
            else:
                raise ValueError(f"Unknown serializer type: {method_type}")
            data = BookSerializer(serializer).serialize_book(book)
            serializing_results.append(data)

        else:
            raise ValueError(f"Unknown command: {cmd}")

    return serializing_results


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
