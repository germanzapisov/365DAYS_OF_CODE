import sqlite3

db = sqlite3.connect('users.db')

cursor = db.cursor()

def creation_table(table):
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        family TEXT NOT NULL
        )
        """
    )
    db.commit()


def add_users(name, family, table):
    cursor.execute(
        f"""
        INSERT INTO {table} (username, family)
        VALUES (?,?)
        """,
        (name, family)
    )
    db.commit()


def show_users(table):
    cursor.execute(
        f"""
        SELECT * FROM {table}
        """
    )
    users = cursor.fetchall()
    print(users)
    db.commit()

