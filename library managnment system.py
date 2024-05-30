class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        print(f"ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nStatus: {'Issued' if self.is_issued else 'Available'}\n")


class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title, author):
        book = Book(self.next_id, title, author)
        self.books.append(book)
        self.next_id += 1
        print("Book added successfully.\n")

    def display_books(self):
        if not self.books:
            print("No books in the library.\n")
            return
        for book in self.books:
            book.display()
            print("-------------------")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print("Book issued successfully.\n")
                else:
                    print("Book is already issued.\n")
                return
        print("Book not found.\n")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print("Book returned successfully.\n")
                else:
                    print("Book is already returned.\n")
                return
        print("Book not found.\n")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display()
                return
        print("Book not found.\n")


def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 6:
            break
        elif choice == 1:
            title = input("Enter title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            book_id = int(input("Enter book ID to issue: "))
            library.issue_book(book_id)
        elif choice == 4:
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id)
        elif choice == 5:
            title = input("Enter title to search: ")
            library.search_book(title)
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()