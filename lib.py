import streamlit as st

library = []
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    
    book = {
        "title": title,
        "author": author,
        "year": year
    } 
    
    library.append(book)
    print(f"Book '{title}' added successfully!")

def view_books():
    if not library:
        print("No books in the library.")
    else:
        print("\nList of Books:")
        for index, book in enumerate(library, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def search_book():
    search_term = input("Enter the title or author of the book to search: ").lower()
    found_books = [book for book in library if search_term in book['title'].lower() or search_term in book['author'].lower()]
    
    if not found_books:
        print("No books found.")
    else:
        print("\nSearch Results:")
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")


def delete_book():
    view_books()
    if not library:
        return 
    
    try:
        book_num = int(input("Enter the number of the book to delete: "))
        if 1 <= book_num <= len(library):
            deleted_book = library.pop(book_num - 1)
            print(f"Book '{deleted_book['title']}' deleted successfully!")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search for a Book")
        print("4. Delete a Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
