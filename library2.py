class Library:
    def __init__(self, book_name, author, available=True):
        """
        Initialize the library book with details.
        :param book_name: str
        :param author: str
        :param available: bool (default is True)
        """
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        """
        Check out a book if available.
        """
        if self.available:
            self.available = False
            print(f"'{self.book_name}' by {self.author} has been checked out.")
        else:
            print(f"'{self.book_name}' by {self.author} is currently unavailable.")

    def return_book(self):
        """
        Return a book to make it available.
        """
        if not self.available:
            self.available = True
            print(f"'{self.book_name}' by {self.author} has been returned and is now available.")
        else:
            print(f"'{self.book_name}' by {self.author} was not checked out.")

    def display_status(self):
        """
        Display the availability status of the book.
        """
        status = "Available" if self.available else "Checked out"
        print(f"'{self.book_name}' by {self.author} is {status}.")

# Example usage:
if __name__ == "__main__":
    # Create a list of book objects
    library_books = [
        Library("1984", "George Orwell"),
        Library("To Kill a Mockingbird", "Harper Lee"),
        Library("The Great Gatsby", "F. Scott Fitzgerald"),
    ]

    while True:
        print("\nLibrary Menu:\n1. Display all books\n2. Check out a book\n3. Return a book\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Books:")
            for book in library_books:
                book.display_status()

        elif choice == "2":
            book_name = input("Enter the name of the book to check out: ")
            for book in library_books:
                if book.book_name.lower() == book_name.lower():
                    book.check_out()
                    break
            else:
                print("Book not found in the library.")

        elif choice == "3":
            book_name = input("Enter the name of the book to return: ")
            for book in library_books:
                if book.book_name.lower() == book_name.lower():
                    book.return_book()
                    break
            else:
                print("Book not found in the library.")

        elif choice == "4":
            print("Exiting the library system. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")
#output 
# Library Menu:
# 1. Display all books
# 2. Check out a book
# 3. Return a book
# 4. Exit
# Enter your choice: 1

# Available Books:
# '1984' by George Orwell is Available.
# 'To Kill a Mockingbird' by Harper Lee is Available.
# 'The Great Gatsby' by F. Scott Fitzgerald is Available.