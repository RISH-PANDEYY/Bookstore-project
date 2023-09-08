import sqlite3

def display_bookstore_info():
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, price FROM books")
    records = cursor.fetchall()

    if records:
        print("Bookstore Database Information:")
        print("-------------------------------")
        for record in records:
            title, author, price = record
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Price: Rs. {price:.2f}")
            print("-------------------------------")
    else:
        print("No records found in the database.")

    conn.close()

def main():
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()

    title = input("Enter the title of the book: ")
    quantity = int(input("Enter the number of copies purchased: "))

    cursor.execute("SELECT price FROM books WHERE title = ?", (title,))
    row = cursor.fetchone()

    if row:
        price = row[0]
        total_amount = price * quantity
        print(f"Total amount for {quantity} copies of '{title}': Rs. {total_amount:.2f}")
    else:
        print("Book not found in the database.")

    conn.close()

if __name__ == "__main__":
    main()
