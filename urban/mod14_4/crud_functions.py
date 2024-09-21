import sqlite3


def initiate_db():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM Products").fetchall()
    connection.close()
    return result
