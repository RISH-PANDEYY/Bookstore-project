import sqlite3

def create_database():
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        price REAL
    )''')

    cursor.execute('''INSERT INTO books (title, author, price)
                      VALUES ('Think Python', 'Allen B. Downey', 475.0)''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
