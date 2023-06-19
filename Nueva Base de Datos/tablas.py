import mysql.connector
from conexion import DatabaseConnection

# Definir la función insert_ingredientes
def insert_ingredientes(connection, id_ingredientes, nombre):
    try:
        cursor = connection.connection.cursor()
        query = "INSERT INTO Ingredientes (idIngredientes, nombre) VALUES (%s, %s)"
        values = (id_ingredientes, nombre)
        cursor.execute(query, values)
        connection.connection.commit()
        print("Ingrediente agregado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al insertar ingrediente:", err)

def insert_Productos(connection, idProductos,Nombre, ingredientes,Precio ):
    try:
        cursor = connection.connection.cursor()
        query = "INSERT INTO Productos (idProductos,Nombre, ingredientes,Precio) VALUES (%s, %s, %s, %s)"
        values = (idProductos,Nombre, ingredientes,Precio)
        cursor.execute(query, values)
        connection.connection.commit()
        print("Productos agregado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al insertar Productos:", err)

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="*****",
    port=3306,
    database="Sandwiches_BigBread"
)

# Establecer la conexión a la base de datos
db_connection.connect()

# Insertar ingredientes con IDs específicos
insert_ingredientes(db_connection, 9, "roquefor")

insert_ingredientes(db_connection, 10, "nuez")

insert_ingredientes(db_connection, 11, "anana")

insert_ingredientes(db_connection, 12, "palmitos")

insert_ingredientes(db_connection, 13, "ternera")

insert_ingredientes(db_connection, 14, "huevo")




# Insertar productos con IDs específicos
insert_Productos(db_connection, 3, "de verdura", 'tomate, jamon, lechuga, queso','350')

insert_Productos(db_connection, 4, "de roquefort", 'roquefot, nuez, jamon','500')

insert_Productos(db_connection, 5, "de rucula", 'jamon crudo, rucula, queso','350')

insert_Productos(db_connection, 6, "de anana", 'jamon , anana','400')

insert_Productos(db_connection, 7, "de palmitos", 'jamon , palmitos','400')

insert_Productos(db_connection, 8, "de ternera y verdura", 'ternera , tomate y huevo','300')

#Crear un Select
cursor = db_connection.connection.cursor()
cursor.execute("SELECT * FROM productos;")
resultados = cursor.fetchall()

for row in resultados:
    print(row[0])

#crear un delete y un update
cursor = conexion.cursor()
consulta = "DELETE FROM pedidos WHERE columna = %s"
valor = ("rodilla",)

cursor.execute(consulta, valor)

cursor = db_connection.connection.cursor()
consulta = "UPDATE Productos SET Precio = %s WHERE Nombre = %s"
valores = (500, "de anana")

cursor.execute(consulta, valor)



cursor.close()

# Cerrar la conexión a la base de datos
db_connection.close()