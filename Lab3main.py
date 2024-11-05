class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}"


class Library:
    def __init__(self):
        self.inventory = {}

    def add_book(self, book):
        if book.isbn in self.inventory:
            self.inventory[book.isbn].quantity += book.quantity
        else:
            self.inventory[book.isbn] = book

    def remove_book(self, isbn, quantity):
        if isbn in self.inventory:
            if self.inventory[isbn].quantity <= quantity:
                del self.inventory[isbn]
            else:
                self.inventory[isbn].quantity -= quantity

    def find_book_by_isbn(self, isbn):
        return self.inventory.get(isbn, None)

    def display_inventory(self):
        for book in self.inventory.values():
            print(book)


# Example Usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("1984", "George Orwell", "1234567890", 5)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9876543210", 3)

    library.add_book(book1)
    library.add_book(book2)

    library.display_inventory()
    library.remove_book("1234567890", 1)
    print("\nAfter removing one copy of 1984:")
    library.display_inventory()
