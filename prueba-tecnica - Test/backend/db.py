import sqlite3

def conexion_db():

    conexion = sqlite3.connect('Mercado.db')
    return conexion

def crear_tabla():

    conexion = conexion_db()
    cursor = conexion.cursor()

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS productos (

                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   precio REAL NOT NULL
                   )
    ''')

    productos = [

        ('Pan', 10000),
        ('Leche', 8000),
        ('Panal de huevos', 18000),
        ('Carne', 20000),
        ('papa', 5000),

    ]

    cursor.execute('SELECT COUNT(*) FROM productos')
    if cursor.fetchone()[0] == 0:
        cursor.executemany('INSERT INTO productos (nombre, precio) VALUES (?,?)', productos)
    
    conexion.commit()
    conexion.close()





    


    

