
from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, item_id, title, price):
        self.__item_id = item_id
        self.__title = title
        self.__price = price

    @property
    def item_id(self):
        return self.__item_id

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    @abstractmethod
    def calculate_fee(self):
        pass

    @abstractmethod
    def display_metadata(self):
        pass

    def __str__(self):
        return f"{self.title} (ID: {self.item_id})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.item_id!r}, {self.title!r})"

    def __eq__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.item_id == other.item_id


class Book(LibraryItem):

    def __init__(self, item_id, title, price, author):
        super().__init__(item_id, title, price)
        self.author = author

    def calculate_fee(self):
        return self.price * 0.05

    def display_metadata(self):
        return f"Book: {self.title}, Author: {self.author}"


class Magazine(LibraryItem):

    def __init__(self, item_id, title, price, issue_number):
        super().__init__(item_id, title, price)
        self.issue_number = issue_number

    def calculate_fee(self):
        return self.price * 0.02

    def display_metadata(self):
        return f"Magazine: {self.title}, Issue: {self.issue_number}"


class DigitalMedia(LibraryItem):

    def __init__(self, item_id, title, price, file_format):
        super().__init__(item_id, title, price)
        self.file_format = file_format

    def calculate_fee(self):
        return self.price * 0.01

    def display_metadata(self):
        return f"Digital Media: {self.title}, Format: {self.file_format}"