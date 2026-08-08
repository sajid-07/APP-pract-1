# Library Management System using OOP

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)
        else:
            print("No books borrowed.")
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add Book
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")

    # Register Patron
    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print("Patron registered successfully!")

    # Find Book
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    # Find Patron
    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name.lower() == name.lower():
                return patron
        return None

    # Issue Book
    def issue_book(self, title, patron_name):
        book = self.find_book(title)
        patron = self.find_patron(patron_name)

        if not book:
            print("Book not found.")
            return

        if not patron:
            print("Patron not found.")
            return

        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print("Book issued successfully!")
        else:
            print("Book is already issued.")

    # Return Book
    def return_book(self, title, patron_name):
        book = self.find_book(title)
        patron = self.find_patron(patron_name)

        if not book or not patron:
            print("Book or Patron not found.")
            return

        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            book.available = True
            print("Book returned successfully!")
        else:
            print("This patron did not borrow this book.")

    # Display Books
    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                book.display()

    # Display Patrons
    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
        else:
            print("\nRegistered Patrons:")
            for patron in self.patrons:
                patron.display()


# -------------------- Main Program --------------------

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(title, author)

    elif choice == "2":
        name = input("Enter Patron Name: ")
        library.register_patron(name)

    elif choice == "3":
        title = input("Enter Book Title: ")
        patron = input("Enter Patron Name: ")
        library.issue_book(title, patron)

    elif choice == "4":
        title = input("Enter Book Title: ")
        patron = input("Enter Patron Name: ")
        library.return_book(title, patron)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")