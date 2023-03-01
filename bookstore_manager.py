# Import the required libraries
import sqlite3

# Define the database name and connect to it
database_name = 'ebookstore.db'
connection = sqlite3.connect(database_name)

# Define the cursor object
cursor = connection.cursor()

#create a function to add books

def add_book():
    # Ask the user for the book details
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    quantity = int(input("Enter the quantity: "))

    # Add the book details to the database
    cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES (?, ?, ?)", (title, author, quantity))
    connection.commit()

    # Print a message to confirm the addition of the book
    print(f"{title} by {author} has been added to the database.")
    
    #create function to update 

def update_book():
        # Ask the user for the book details
    book_id = int(input("Enter the book ID: "))
    title = input("Enter the new title (leave blank to keep the same): ")
    author = input("Enter the new author (leave blank to keep the same): ")
    quantity = input("Enter the new quantity (leave blank to keep the same): ")

    # Update the book details in the database
    if title != "":
        cursor.execute("UPDATE books SET Title = ? WHERE id = ?", (title, book_id))
    if author != "":
        cursor.execute("UPDATE books SET Author = ? WHERE id = ?", (author, book_id))
    if quantity != "":
        cursor.execute("UPDATE books SET Qty = ? WHERE id = ?", (quantity, book_id))

    connection.commit()

    # Print a message to confirm the update of the book
    print(f"Book with ID {book_id} has been updated.")


def delete_book():
    # Ask the user for the book ID
    book_id = int(input("Enter the book ID: "))

    # Delete the book from the database
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    connection.commit()

    # Print a message to confirm the deletion of the book
    print(f"Book with ID {book_id} has been deleted.")

def search_book():
    # Ask the user for the search query
    search_query = input("Enter the search query: ")

    # Search for the book in the database
    cursor.execute("SELECT * FROM books WHERE Title LIKE ? OR Author LIKE ?", ('%' + search_query + '%', '%' + search_query + '%'))

    # Print the search results
    print("Search Results:")
    print("ID\tTitle\t\t\tAuthor\t\tQty")
    for book in cursor.fetchall():
        print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}")
# Define the main menu
menu = """Welcome to the ebookstore database. Please select an option:
1. Add a new book
2. Update book information
3. Delete a book
4. Search for a book
5. Quit
"""

# Define a loop to keep the menu running

while True:
    # Display the main menu and ask the user for their choice
    choice = input(menu)

    # Call the appropriate function based on the user's choice
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        # Quit the program
        print("Goodbye!")
        break
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")
        
        
        
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('ebookstore.db')
c = conn.cursor()

# Create the books table
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              qty INTEGER)''')

# Populate the books table with some initial data
c.execute("INSERT INTO books VALUES (3001, 'A Tale of Two Cities', 'Charles Dickens', 30)")
c.execute("INSERT INTO books VALUES (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40)")
c.execute("INSERT INTO books VALUES (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25)")
c.execute("INSERT INTO books VALUES (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37)")
c.execute("INSERT INTO books VALUES (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)")

# Save the changes
conn.commit()

# Define the main menu
menu = """
Please select an option:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
"""

# Function to add a book to the database
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    qty = input("Enter the quantity of the book: ")
    c.execute("INSERT INTO books (title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
    print("Book added successfully!")
    conn.commit()

# Function to update a book in the database
def update_book():
    book_id = input("Enter the ID of the book you want to update: ")
    title = input("Enter the new title of the book: ")
    author = input("Enter the new author of the book: ")
    qty = input("Enter the new quantity of the book: ")
    c.execute("UPDATE books SET title=?, author=?, qty=? WHERE id=?", (title, author, qty, book_id))
    print("Book updated successfully!")
    conn.commit()

# Function to delete a book from the database
def delete_book():
    book_id = input("Enter the ID of the book you want to delete: ")
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    print("Book deleted successfully!")
    conn.commit()

# Function to search for a book in the database
def search_book():
    search_term = input("Enter the title or author of the book you want to search for: ")
    c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%'+search_term+'%', '%'+search_term+'%'))
    results = c.fetchall()
    if len(results) == 0:
        print("No books found.")
    else:
        for row in results:
            print(row)

# Main loop
while True:
    # Display the main menu and ask the user for their choice
    choice = input(menu)

    # Call the appropriate function based on the user's choice
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_book()
    elif choice == "0":
        # Quit the program
        print("Goodbye!")
        break
    else:
        print("invalid choice")


# Close the database connection
conn.close()
