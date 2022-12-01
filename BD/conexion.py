import mysql.connector
from mysql.connector import Error
from colorama import Fore, init


class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='nahuel007',
                db='mundialqatar'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarJugadores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM qatar")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(Fore.RED +"Error al intentar la conexión: {0}".format(ex))
    
    def listarEquipos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT distinct equipo FROM qatar")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarJugadores(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO qatar (id,equipo,nombre,apellido,nroCamiseta,posicion,nroGoles,nroPartidasGanadasEquipo,edad,peso,altura) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')"
                cursor.execute(sql.format(curso[0], curso[1],curso[2],curso[3],curso[4],curso[5],curso[6],curso[7],curso[8],curso[9],curso[10]))
                self.conexion.commit()
                print("¡Jugador registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarJugadores(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE qatar SET equipo = '{0}',nombre = '{1}',apellido = '{2}',nroCamiseta = '{3}',posicion = '{4}',nroGoles = '{5}',nroPartidasGanadasEquipo = '{6}',edad = '{7}',peso = '{8}',altura = '{9}' WHERE id = '{10}'"
                cursor.execute(sql.format(curso[1],curso[2],curso[3],curso[4],curso[5],curso[6],curso[7],curso[8],curso[9],curso[10],curso[0]))
                self.conexion.commit()
                print("¡Jugador actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarJugadores(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'DELETE FROM qatar WHERE id = "{0}"'
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("¡Jugador eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def eliminarEquipo(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'DELETE FROM qatar WHERE equipo = "{0}"'
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("¡Jugador eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
