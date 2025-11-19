import sqlite3

connect = sqlite3.connect('cars.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (20) NOT NULL,
    age INTEGER NOT NULL,
    color VARCHAR (15)
    )
''')
connect.commit()

# CRUD - Create Read Update Delete

def create_car(name, age, color):
    cursor.execute(
        'INSERT INTO cars(name, age, color) VALUES(?, ?, ?)',
        (name, age, color)
    )
    connect.commit()
    print(f"Create car - '{name}'!!!")

# create_car("Toyota", 2011, "Black")
# create_car("Mercedes-Benz", 2022, "White")
# create_car("Subaru", 2017, "Green")
# create_car("BMW", 2023, "Gold")

def read_cars():
    cursor.execute('SELECT name FROM cars')
    cars = cursor.fatchall()
    print(cars)

def detail_cars(id):
    cursor.execute(
        'SELECT name, age, color FROM cars WHERE id = ?',
        (id,)
    )
    cars = cursor.fetchone()
    print(cars)

# detail_cars(1)

def update_cars(name, id):
    cursor.execute(
        'UPDATE cars SET name = ? WHERE id = ?',
        (name, id)
    )
    connect.commit()
    print(f"Car with id - {id} updated")


# update_cars("Mercedes-Benz", 4)


def delete_cars(id):
    cursor.execute('DELETE FROM cars WHERE id = ?', (id,))
    connect.commit()
    print(f"Cars with id {id} deleted")

delete_cars(4)




