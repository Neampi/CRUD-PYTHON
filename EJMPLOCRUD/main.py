
import os, sys
from PyQt5 import *
from PyQt5 import QtWidgets
import PySide2
from conexion_bd import Comunicacion
from ui_diseno import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bt_menu.clicked.connect(self.mover_menu)

        self.base_datos=Comunicacion()


        #BOTONES
            #BASE DE DATOS MOSTRAR
        self.ui.bt_refrescar.clicked.connect(self.mostrar_productos)
            #REGISTRAR
        self.ui.bt_registrar_registrar.clicked.connect(self.registrar_productos)
            #ELIMINAR
        self.ui.bt_buscar_eliminar.clicked.connect(self.buscar_por_nombre_eliminar)
        self.ui.bt_eliminar_eliminar.clicked.connect(self.eliminar_productos)
            #ACTUALIZAR
        self.ui.bt_buscar_actualizar.clicked.connect(self.buscar_por_nombre_actualizar)
        self.ui.bt_actualizar_actualizar.clicked.connect(self.modificar_productos)


        #BOTONES TITULO
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())


        #ELIMINAR BARRA DE TITULO
        self.setWindowFlag(Qt.FramelessWindowHint)


        #MOVER VENTANA
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

        #CONEXION BOTONES
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_datos)
        self.ui.bt_basedatos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_datos))
        self.ui.bt_registrar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_registrar))
        self.ui.bt_actualizar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_actualizar))
        self.ui.bt_eliminar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_eliminar))
        self.ui.bt_ajustes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ajustes))

        #AJUSTE DE TABLAS
        self.ui.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_maximizar(self):
        self.showMaximized()


    ##MOVER VENTANA
    def mousePressEvent(self, event):
        self.click_position=event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized()==False:
            if event.buttons()==Qt.LeftButton:
                self.move(self.pos()+event.globalPos()-self.click_position)
                self.click_position=event.globalPos()
                event.accept()
        
    #MOVER MENU
    def mover_menu(self):
        if True:
            width=self.ui.frame_control.width()
            normal=0
            if width==0:
                extender=200
            else:
                extender=normal
            self.animacion = QPropertyAnimation(self.ui.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
            self.animacion.start()

    #CONFIGURACION BASE DE DATOS
    def mostrar_productos(self):
        datos=self.base_datos.mostrar_productos()
        i=len(datos)
        self.ui.tabla_productos.setRowCount(i)
        tablerow=0
        for row in datos:
            self.ui.tabla_productos.setItem(tablerow,0,QTableWidgetItem(row[0]))
            self.ui.tabla_productos.setItem(tablerow,1,QTableWidgetItem(row[1]))
            self.ui.tabla_productos.setItem(tablerow,2,QTableWidgetItem(row[2]))
            self.ui.tabla_productos.setItem(tablerow,3,QTableWidgetItem(row[3]))
            self.ui.tabla_productos.setItem(tablerow,4,QTableWidgetItem(row[4]))
            self.ui.tabla_productos.setItem(tablerow,5,QTableWidgetItem(row[5]))
            tablerow=+1
            self.ui.signal_actualizar.setText("")
            self.ui.signal_registrar.setText("")
            self.ui.signal_eliminar.setText("")

    #REGISTRO DE PRODUCTOS
    def registrar_productos(self):
        codigo=self.ui.codigo_reg.text()
        nombre=self.ui.nom_reg.text()
        modelo=self.ui.modelo_reg.text()
        precio=self.ui.pre_reg.text()
        cantidad=self.ui.cantidad_red.text()

        if codigo!='' and nombre!='' and modelo!='' and precio!='' and cantidad!='':
            self.base_datos.insertar_producto(codigo,nombre,modelo,precio,cantidad)
            self.ui.signal_registrar.setText("Producto Registrado")
            self.ui.codigo_reg.clear()
            self.ui.nom_reg.clear()
            self.ui.modelo_reg.clear()
            self.ui.pre_reg.clear()
            self.ui.cantidad_red.clear()
        else:
            self.ui.signal_registrar.setText("Datos Incompletos")

    def buscar_por_nombre_actualizar(self):
        id_producto=self.ui.princ_buscar.text()
        self.producto=self.base_datos.buscar_producto(id_producto)
        if len(self.producto)!=0:
            self.Id=self.producto[0][0]
            self.ui.cod_buscar.setText(self.producto[0][1])
            self.ui.nombre_buscar.setText(self.producto[0][2])
            self.ui.modelo_buscar.setText(self.producto[0][3])
            self.ui.precio_buscar.setText(self.producto[0][4])
            self.ui.cantidad_buscar.setText(self.producto[0][5])
        else:
            self.ui.signal_actualizar.setText("NO EXISTE")

    def modificar_productos(self):
        if self.producto!='':
            codigo=self.ui.cod_buscar.text()
            nombre=self.ui.nombre_buscar.text()
            modelo=self.ui.modelo_buscar.text()
            precio=self.ui.precio_buscar.text()
            cantidad=self.ui.cantidad_buscar.text()

            actualizar=self.base_datos.actualizar_datos(self.Id,codigo,nombre,modelo,precio,cantidad)
            if actualizar==1:
                self.ui.signal_actualizar.setText("ACTUALIZADO")
                self.ui.cod_buscar.clear()
                self.ui.nombre_buscar.clear()
                self.ui.modelo_buscar.clear()
                self.ui.precio_buscar.clear()
                self.ui.cantidad_buscar.clear()
                self.ui.princ_buscar.setText("")
            elif actualizar==0:
                self.ui.signal_actualizar.setText("ERROR")
            else:
                self.ui.signal_actualizar.setText("INCORRECTO")

    def buscar_por_nombre_eliminar(self):
        nombre_producto=self.ui.eliminar_buscar.text()
        producto=self.base_datos.buscar_producto(nombre_producto)
        self.ui.tabla_borrar.setRowCount(len(producto))

        if len(producto)==0:
            self.ui.signal_eliminar.setText("No Existe")
        else: 
            self.ui.signal_eliminar.setText("Producto Seleccionado")
        tablerow=0
        for row in producto:
            self.producto_a_borrar=row[2]
            self.ui.tabla_borrar.setItem(tablerow,0,QTableWidgetItem(row[0]))
            self.ui.tabla_borrar.setItem(tablerow,1,QTableWidgetItem(row[1]))
            self.ui.tabla_borrar.setItem(tablerow,2,QTableWidgetItem(row[2]))
            self.ui.tabla_borrar.setItem(tablerow,3,QTableWidgetItem(row[3]))
            self.ui.tabla_borrar.setItem(tablerow,4,QTableWidgetItem(row[4]))
            self.ui.tabla_borrar.setItem(tablerow,5,QTableWidgetItem(row[5]))
            tablerow+=1
        
    def eliminar_productos(self):
        self.row_flag=self.ui.tabla_borrar.currentRow()
        if self.row_flag==0:
            self.ui.tabla_borrar.removeRow(0)
            self.base_datos.eliminar_productos(self.producto_a_borrar)
            self.ui.signal_eliminar.setText("Producto Eliminado")
            self.ui.eliminar_buscar.setText("")

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())


