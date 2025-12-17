import sqlite3

# Connect to database


connection = sqlite3.connect('bookstore.db')
cursor = connection.cursor()


# Create books table


def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                      (id INTEGER PRIMARY KEY,
                       title TEXT,
                       authorID INTEGER,
                       qty INTEGER)''')
    connection.commit()

def create_table_author():
    cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                       id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       country TEXT
                   )''')
    connection.commit()


# Add default books


def add_default_books():
    books = [
        (3001, 'Tale of Two Cities', 1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 2356, 25),
        (3004, 'The Lord of the Rings', 6380, 37),
        (3005, "Alice's Adventures in Wonderland", 5620, 12),
        (3006, 'The Story behind Walls', 2210, 18),
        (3007, 'The Punisher', 1366, 10)
    ]
    cursor.executemany('INSERT OR IGNORE INTO books \
        (id, title, authorID, qty) VALUES (?, ?, ?, ?)', books)
    connection.commit()


# Add default authors


def add_default_authors():
    authors = [
        (1290, 'Charles Dickens', 'England'),
        (8937, 'J.K. Rowling', 'England'),
        (2356, 'C.S. Lewis', 'Ireland'),
        (6380, 'J.R.R. Tolkien', 'South Africa'),
        (5620, 'Lewis Carroll', 'England'),
        (2210, 'Johnsen Paul', 'Portugal'),
        (1366, 'Benny Tripen', 'Spain')
    ]
    cursor.executemany('INSERT OR IGNORE INTO authors \
        (id, name, country) VALUES (?, ?, ?)', authors)
    connection.commit()


# Add a new book record


def add_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    authorID = int(input("Enter author ID: "))
    qty = int(input("Enter quantity: "))
    cursor.execute('INSERT INTO books (id, title, authorID, qty) \
        VALUES (?, ?, ?, ?)', (id, title, authorID, qty))
    connection.commit()
    print("Book added successfully!\n")

# View Books with Author Details using inner join

def view_books_with_authors():
    cursor.execute('''SELECT books.id, books.title, books.qty, authors.name, authors.country
                      FROM books
                      INNER JOIN authors ON books.authorID = authors.id''')
    rows = cursor.fetchall()
    print("\n--- Book List ---")
    for row in rows:
        print(
            f"ID: {row[0]}, Title: {row[1]}, Qty: {row[2]}, Author: {row[3]}, Country: {row[4]}"
        )
    print()


# Update the book record


def update_book():
    book_id = int(input("Enter book ID to update: "))
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    if not book:
        print("Book not found.\n")
        return

    print("1. Update title\n2. Update author ID\n3. Update quantity")
    option = input("Choose an option: ").strip()

    if option == '1':
        new_title = input("Enter new title: ")
        cursor.execute("UPDATE books SET title = ? WHERE id = ?", (new_title, book_id))
    elif option == '2':
        new_author = int(input("Enter new author ID: "))
        cursor.execute("UPDATE books SET authorID = ? WHERE id = ?", (new_author, book_id))
    elif option == '3':
        new_qty = int(input("Enter new quantity: "))
        cursor.execute("UPDATE books SET qty = ? WHERE id = ?", (new_qty, book_id))
    else:
        print("Invalid option.")
        return

    connection.commit()
    print("Book updated successfully!\n")


# Delete a book record


def delete_book():
    book_id = int(input("Enter book ID to delete: "))
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    print("Book deleted successfully!\n")


# Search for a book by ID, title, or author ID


def search_book():
    search_term = input("Enter book ID, title, or author ID to search: ")
    cursor.execute("SELECT * FROM books WHERE id = ? OR title = ? OR authorID = ?",
                   (search_term, search_term, search_term))
    book = cursor.fetchone()
    if book:
        print("Book found:", book, "\n")
    else:
        print("No matching book found.\n")


# --- Setup and Main Menu ---


create_table()
create_table_author()
add_default_authors()
add_default_books()

while True:
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search book")
    print("5. View details of all books")
    print("0. Exit")
    choice = input("Select an option: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        view_books_with_authors()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.\n")


# Close connection


connection.close()
