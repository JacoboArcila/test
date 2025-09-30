#Funcion tipo get para listar todos los productos:

def listar_productos(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombre, precio FROM productos')

    filas = cursor.fetchall()

    productos = []

    for fila in filas:

        productos.append({

            'id' : fila[0],
            'nombre' : fila[1],
            'precio' : fila[2],
    })
        
    return productos


#Otro metodo get pero para buscar por ID de producto

def buscar_producto(conexion, usuario_id):

    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombre, precio FROM productos WHERE id = ?', (usuario_id,))

    fila = cursor.fetchone()

    if fila:

        return {

            'id' : fila[0],
            'nombre' : fila[1],
            'precio' : fila[2],
        }
    
    return None


#Metodo POST para agregar un producto

def agregar_producto (conexion, nombre, precio):

    cursor = conexion.cursor()
    cursor.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (nombre, precio))
    conexion.commit()

    return 'Producto agregado correctamente'
    
