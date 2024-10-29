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

def buscarUnaNota():
    print("Buscar una nota".center(50, "="))
    cursor, connection = conexionMysql()
    if cursor:
        nombreABuscar = input("Ingresa el titulo a buscar: ")
        cursor.execute(
            f"SELECT * FROM tareas where nombre like '%{nombreABuscar}%' and idUsuario = {idUsuario} Limit 1"
        )
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        opcionFantasma = input("presiona lo que sea para salir")
        cerrarConexiones(cursor, connection)


def buscarUnaNotaComplemento():
    print("Buscar un usuario".center(50, "="))
    cursor, connection = conexionMysql()
    if cursor:
        nombreABuscar = input("Ingresa el usuario a buscar: ")
        cursor.execute(
            f"SELECT * FROM tareas where nombre like '%{nombreABuscar}%' and idUsuario = {idUsuario} Limit 1"
        )
        myresult = cursor.fetchall()
        if myresult != "":
            for x in myresult:
                print(x)
            cerrarConexiones(cursor, connection)
            return myresult
        else:
            return "no hay notas"


opcion = 1
while opcion != 0:
    print("""Iniciar sesion
        """)
    usuario = input("Ingresa tu usuario: ")
    password = input("Password: ")
    cursor, conexion = conexionMysql()

    if cursor:
        cursor.execute(
            f"SELECT * FROM usuarios where usuario like '%{usuario}%' and password = '{password}'"
        )
        myresult = cursor.fetchall()
        if myresult:
            cerrarConexiones(cursor, conexion)
            idUsuario = myresult[0][0]
            print("Bienvenido".center(50, "="))
            opcionSistema = 1
            while opcion != 0:
                print("""
        1.- generar nota
        2.- consultar tus notas
        3.- consultar una nota
        4.- modificar nota
        5.- borrar nota
        0.- salir
                    """)
                opcionSistema = int(input("Ingresa tu opcion: "))

                if opcionSistema == 1:
                    print("Generar  nota".center(50, "="))
                    cursor, connection = conexionMysql()
                    if cursor:
                        nombre = input("Ingresa el nombre: ")
                        descripcion = input("Ingresa tu descripcion: ")
                        sql = f"INSERT INTO `sistematodo`.`tareas` (`idUsuario`, `nombre`, `descripcion`, `status`) VALUES ({idUsuario}, '{nombre}', '{descripcion}', 0);"
                        cursor.execute(sql)
                        connection.commit()
                        print(cursor.rowcount, "record inserted.")
                        opcionFantasma = input("presiona lo que sea para salir")
                        cerrarConexiones(cursor, connection)

                if opcionSistema == 2:
                    print("Mostrar todos las notas".center(50, "="))
                    cursor, connection = conexionMysql()
                    if cursor:
                        cursor.execute(f"SELECT * FROM tareas where idUsuario = {idUsuario}")
                        myresult = cursor.fetchall()
                        for x in myresult:
                            print(x)
                        opcionFantasma = input("presiona lo que sea para salir")
                        cerrarConexiones(cursor, connection)

                if opcionSistema == 3:
                    buscarUnaNota()

                if opcionSistema == 4:
                    print("Modificar nota".center(50, "="))
                    id = buscarUnaNotaComplemento()
                    idNota = id[0][0]
                    verificacion = input("Este es la nota que quieres modificar?")
                    if verificacion.lower() == "si":
                        cursor, connection = conexionMysql()
                        nombre = input("Ingresa en nombre de la nota: ")
                        descripcion = input("Ingresa la descripcion: ")
                        sql = f"UPDATE `sistematodo`.`tareas` SET `nombre`='{nombre}', `descripcion`='{descripcion}' WHERE `id`={idNota};"
                        cursor.execute(sql)
                        connection.commit()
                        print(cursor.rowcount, "record updated.")
                        opcionFantasma = input("presiona lo que sea para salir")
                        cerrarConexiones(cursor, connection)
                    else:
                        print("Realiza otra busqueda")
                        opcionFantasma = input("presiona lo que sea para salir")
                if opcionSistema == 5:
                    print("Eliminar nota".center(50, "="))
                    id = buscarUnaNotaComplemento()
                    idNota = id[0][0]
                    verificacion = input("Este es la nota que quieres eliminar?")
                    if verificacion.lower() == "si":
                        cursor, connection = conexionMysql()
                        sql = f"DELETE FROM `sistematodo`.`tareas` WHERE  `id`={idNota};"
                        cursor.execute(sql)
                        connection.commit()
                        print(cursor.rowcount, "record deleted.")
                        opcionFantasma = input("presiona lo que sea para salir")
                        cerrarConexiones(cursor, connection)
                    else:
                        print("Realiza otra busqueda")
                        opcionFantasma = input("presiona lo que sea para salir")
                if opcionSistema == 0:
                    opcion = 0
        else:
            print("ingresa un usuario valido")
print("adios")
