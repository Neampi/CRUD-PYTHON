
import sqlite3

class Comunicacion():
    def __inif__(self):
        self.conexion=sqlite3.connect('ejemplo.db')

    def insertar_producto(self,codigo,nombre,modelo,precio,cantidad):
        self.conexion=sqlite3.connect('ejemplo.db')
        cursor=self.conexion.cursor()
        script='INSERT INTO tabla_datos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) VALUES(?,?,?,?,?)'
        cursor.execute(script,(codigo,nombre,modelo,precio,cantidad,))
        self.conexion.commit()
        cursor.close()

    def mostrar_productos(self):
        self.conexion=sqlite3.connect('ejemplo.db')
        cursor=self.conexion.cursor()
        script='SELECT * FROM tabla_datos'
        cursor.execute(script)
        registro=cursor.fetchall()
        return registro

    def buscar_producto(self, nombre_producto):
        self.conexion=sqlite3.connect('ejemplo.db')
        cursor=self.conexion.cursor()
        script='SELECT * FROM tabla_datos WHERE NOMBRE = ?'
        cursor.execute(script,(nombre_producto,))
        nombreX=cursor.fetchall()
        cursor.close()
        return nombreX

    def eliminar_productos(self, nombre):
        cursor=self.conexion.cursor()
        script='DELETE FROM tabla_datos WHERE NOMBRE = ?'
        cursor.execute(script,(nombre,))
        self.conexion.commit()
        cursor.close()

    def actualizar_datos(self,id,codigo,nombre,modelo,precio,cantidad):
        cursor=self.conexion.cursor()
        script='UPDATE tabla_datos SET CODIGO=?, NOMBRE=?, MODELO=?, PRECIO=?, CANTIDAD=? WHERE ID=?'
        cursor.execute(script,(codigo,nombre,modelo,precio,cantidad,id))
        a=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
