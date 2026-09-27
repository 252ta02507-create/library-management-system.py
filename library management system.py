# Library Management System

books = []


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!")


def view_books():
    if not books:
        print("No books available.")
        return

    print("\n--- Library Books ---")

    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {book['status']}")
        print("------------------------")


def search_book():
    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found")
            print(f"Title : {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Status: {book['status']}")
            return

    print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book returned successfully!")
            else:
                print("Book is already available.")
            return

    print("Book not found.")


while True:
    print("\n==============================")
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
