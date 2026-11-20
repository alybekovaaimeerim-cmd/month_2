import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL,
    year INTEGER
)
""")

connection.commit()


def create_book(title, author, price, year):
    cursor.execute(
        "INSERT INTO books (title, author, price, year) VALUES (?, ?, ?, ?)",
        (title, author, price, year)
    )
    connection.commit()


def read_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    for book in books:
        print(book)


def update_book(id, price):
    cursor.execute(
        "UPDATE books SET price = ? WHERE id = ?",
        (price, id)
    )
    connection.commit()


def delete_book(id):
    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (id,)
    )
    connection.commit()


create_book("1984", "George Orwell", 500, 1949)
create_book("Маленький принц", "Антуан де Сент-Экзюпери", 400, 1943)

print("Все книги:")
read_books()

print("После изменения цены:")
update_book(1, 600)
read_books()

print("После удаления:")
delete_book(2)
read_books()

connection.close()