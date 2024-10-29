import mysql.connector
from mysql.connector import Error


def conexionMysql():
    try:
        connection = mysql.connector.connect(
            host="localhost", user="python", password="python", database="sistemaTodo"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            return cursor, connection
    except Error as e:
        print("Error al conectar a MySQL:", e)
        return None, None


def cerrarConexiones(cursor, connection):
    cursor.close()
    connection.close()


def buscarUnUsuario():
    print("Buscar un usuario".center(50, "="))
    cursor, connection = conexionMysql()
    if cursor:
        nombreABuscar = input("Ingresa el usuario a buscar: ")
        cursor.execute(
            f"SELECT * FROM usuarios where nombre like '%{nombreABuscar}%' Limit 1"
        )
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        opcionFantasma = input("presiona lo que sea para salir")
        cerrarConexiones(cursor, connection)


def buscarUnUsuarioComplento():
    print("Buscar un usuario".center(50, "="))
    cursor, connection = conexionMysql()
    if cursor:
        nombreABuscar = input("Ingresa el usuario a buscar: ")
        cursor.execute(
            f"SELECT * FROM usuarios where nombre like '%{nombreABuscar}%' Limit 1"
        )
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        cerrarConexiones(cursor, connection)
        return myresult[0]


opcion = 1
while opcion != 0:
    print("""
        1.- generar usuarios
        2.- consultar todos usuarios
        3.- consultar un usuario
        4.- modificar usuarios
        5.- borrar usuarios
        0.- salir
        """)
    opcion = int(input("Ingresa tu opcion: "))

    if opcion == 1:
        print("Generar usuarios".center(50, "="))
        cursor, connection = conexionMysql()
        if cursor:
            nombre = input("Ingresa tu nombre: ")
            usuario = input("Ingresa tu usuario: ")
            password = input("Ingresa tu password: ")
            sql = f"INSERT INTO `sistematodo`.`usuarios` (`nombre`, `usuario`, `password`) VALUES ('{nombre}', '{usuario}', '{password}');"

            cursor.execute(sql)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
            opcionFantasma = input("presiona lo que sea para salir")
            cerrarConexiones(cursor, connection)

    if opcion == 2:
        print("Mostrar todos los usuarios".center(50, "="))
        cursor, connection = conexionMysql()
        if cursor:
            cursor.execute("SELECT * FROM usuarios")
            myresult = cursor.fetchall()
            for x in myresult:
                print(x)
            opcionFantasma = input("presiona lo que sea para salir")
            cerrarConexiones(cursor, connection)

    if opcion == 3:
        buscarUnUsuario()

    if opcion == 4:
        print("Modificar usuario".center(50, "="))
        id = buscarUnUsuarioComplento()
        id = id[0]
        verificacion = input("Este es el usuario que quieres modificar?")
        if verificacion.lower() == "si":
            cursor, connection = conexionMysql()
            nombre = input("Ingresa tu nombre: ")
            usuario = input("Ingresa tu usuario: ")
            password = input("Ingresa tu password: ")
            sql = f"UPDATE `sistematodo`.`usuarios` SET `nombre`='{nombre}', `usuario`='{usuario}', `password`='{password}' WHERE  `id`={id};"
            cursor.execute(sql)
            connection.commit()
            print(cursor.rowcount, "record updated.")
            opcionFantasma = input("presiona lo que sea para salir")
            cerrarConexiones(cursor, connection)
        else:
            print("Realiza otra busqueda")
            opcionFantasma = input("presiona lo que sea para salir")
    if opcion == 5:
        print("Eliminar usuario".center(50, "="))
        id = buscarUnUsuarioComplento()
        id = id[0]
        verificacion = input("Este es el usuario que quieres modificar?")
        if verificacion.lower() == "si":
            cursor, connection = conexionMysql()
            sql = f"DELETE FROM `sistematodo`.`usuarios` WHERE  `id`={id};"
            cursor.execute(sql)
            connection.commit()
            print(cursor.rowcount, "record deleted.")
            opcionFantasma = input("presiona lo que sea para salir")
            cerrarConexiones(cursor, connection)
        else:
            print("Realiza otra busqueda")
            opcionFantasma = input("presiona lo que sea para salir")
