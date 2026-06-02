import sqlite3

db = sqlite3.connect('database.db')

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS database (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    family TEXT NOT NULL
    )
""")

def add_customers(username, name, family):
    cursor.execute("""
        INSERT INTO database (username, name, family)
        VALUES (?,?,?)
    """, (username, name, family))

def show_customers():
    cursor.execute("""
    SELECT * FROM database 
    ORDER BY id
    LIMIT 100
    """)


    database_text = cursor.fetchall()

    for i in database_text:
        print(i)

def add_column(column):
    cursor.execute(f"""
    ALTER TABLE database
    add column {column}
    """)

def update_table(new_name, new_family, customer_id):
    cursor.execute("""
    UPDATE database
    SET name = ?,
    family = ?
    WHERE id = ?
    """, (new_name, new_family, customer_id))

def delete_customers(id):
    cursor.execute(f"""
    DELETE FROM database
    WHERE id={id}
    """)


def delete_table():
    cursor.execute("""
    DROP TABLE database
    """)

def menu(db):
    while True:
        asc = int(input
                  ("""
           Enter the desired action:
            1 > Add user to table
            2 > Remove user from table by ID
            3 > List users in table
            4 > Add column to table
            5 > Edit client data by ID
            6 > Delete table
            7 - Undo last changes
            8 > Exit adding tool
            >>>
        """)
                  )
        if asc == 1:
            username = input('Enter nickname: ')
            name = input('Enter first name: ')
            family = input('Enter last name: ')
            add_customers(username, name, family)
        elif asc == 2:
            id_for_delete = input("Enter id to delete")
            delete_customers(id_for_delete)
        elif asc == 3:
            show_customers()
        elif asc == 4:
            column = input("Enter the column name: ")
            add_column(column)
        elif asc == 5:
            customer_id = int(input("Enter the person ID to change"))
            new_name = input("Enter the new customer name: ")
            new_family = input("Enter the new customer last name: ")
            update_table(new_name, new_family, customer_id)
        elif asc == 6:
            delete_table()
        elif asc == 7:
            db.rollback()
        else:
            db.commit()
            db.close()
            exit()



menu(db)
