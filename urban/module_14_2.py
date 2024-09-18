import sqlite3

connection = sqlite3.connect("../not_telegram.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id       INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email    TEXT NOT NULL,
        age      INTEGER,
        balance  INTEGER NOT NULL
    )
""")

# Заполним таблицу 10-ю записями:
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))


# Обновите balance у каждой 2-ой записи начиная с 1-ой на 500:
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))


# Удалите каждую 3-ю запись в таблице начиная с 1-ой:
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))


# Сделайте выборку всех записей при помощи fetchall(),
# где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute("SELECT * FROM Users WHERE age != 60")
records = cursor.fetchall()
for rec in records:
    print("Имя: {1} | Почта: {2} | Возраст: {3} | Баланс: {4}".format(*rec))


# Удалите из базы данных not_telegram.db запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))


# Подсчёт кол-ва всех пользователей
# Подсчёт суммы всех балансов
cursor.execute("SELECT COUNT(*), SUM(balance) FROM Users")
total_users, all_balances = cursor.fetchone()
print("-" * 25)
print("Средний баланс:",  all_balances / total_users)

connection.commit()
connection.close()
