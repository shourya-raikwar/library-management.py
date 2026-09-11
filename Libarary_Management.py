# Library Management System

books = []


def add_book():
    book_id = input("Book ID: ")
    title = input("Book Title: ")
    author = input("Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    print("Book successfully added!\n")


def display_books():
    if not books:
        print("Library mein koi book nahi hai.\n")
        return

    print("\n--- All Books ---")
    for book in books:
        status = "Issued" if book["issued"] else "Available"

        print("Book ID   :", book["id"])
        print("Title     :", book["title"])
        print("Author    :", book["author"])
        print("Status    :", status)
        print("------------------------")


def search_book():
    keyword = input("Book title ya author name enter karein: ").lower()

    found = False

    for book in books:
        if (keyword in book["title"].lower()
                or keyword in book["author"].lower()):

            status = "Issued" if book["issued"] else "Available"

            print("\nBook ID :", book["id"])
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            print("Status  :", status)

            found = True

    if not found:
        print("Book nahi mili.\n")


def issue_book():
    book_id = input("Issue karne ke liye Book ID enter karein: ")

    for book in books:
        if book["id"] == book_id:

            if book["issued"]:
                print("Ye book already issued hai.\n")
            else:
                book["issued"] = True
                print("Book successfully issued!\n")

            return

    print("Book ID nahi mili.\n")


def return_book():
    book_id = input("Return karne ke liye Book ID enter karein: ")

    for book in books:
        if book["id"] == book_id:

            if not book["issued"]:
                print("Ye book already library mein available hai.\n")
            else:
                book["issued"] = False
                print("Book successfully returned!\n")

            return

    print("Book ID nahi mili.\n")


def main():
    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        print("===============================================")

        choice = input("Apna choice enter karein: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please try again.\n")


# Program start
main()
