import json
from abc import abstractmethod, ABC
import xml.etree.ElementTree as ET
from app.books import Book


class Serializer(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):

    def serialize(self, book):
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):

    def serialize(self, book):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class BookSerializer:

    def __init__(self, serializer: Serializer):
        self.serializer = serializer

    def serialize_book(self, book: Book):
        return self.serializer.serialize(book)
