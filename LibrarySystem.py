from abc import ABC, abstractmethod

class LibraryItem(ABC):
    item_count = 0

    def __init__(self, title="Unknown", year=0):
        self.title = title
        self.year = year
        LibraryItem.item_count += 1

    @abstractmethod
    def displayInfo(self):
        pass

    @classmethod
    def get_item_count(cls):
        return cls.item_count


class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def displayInfo(self):
        print(f"Book: {self.title}")
        print(f"Year: {self.year}")
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, year, duration, genre):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    def displayInfo(self):
        print(f"DVD: {self.title}")
        print(f"Year: {self.year}")
        print(f"Duration: {self.duration} mins")
        print(f"Genre: {self.genre}")


if __name__ == "__main__":
    items = [
        Book("Java Basics", 2020, "John Doe"),
        DVD("Inception", 2010, 148, "Sci-Fi")
    ]

    for item in items:
        print("\n--- Item Info ---")
        item.displayInfo()

    print("\nTotal Items:", LibraryItem.get_item_count())