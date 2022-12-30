# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dise�ocRuGNh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 487)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #000000ff;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(16, 255, 255);\n"
"    border-radius:20px;\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 0))
        icon = QIcon()
        icon.addFile(u"../../icons/svg/043.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(425, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"../../icons/svg/278.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.bt_minimizar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"../../icons/svg/254.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon2)
        self.bt_maximizar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"../../icons/svg/057.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon3)
        self.bt_cerrar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.bt_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_contenido)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(200, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 206, 151);\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(100, 202, 193);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"	font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  white;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"    color: rgb(0, 0, 0);\n"
"	font: 77 10pt \"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bt_basedatos = QPushButton(self.frame_control)
        self.bt_basedatos.setObjectName(u"bt_basedatos")
        self.bt_basedatos.setMinimumSize(QSize(0, 40))
        icon4 = QIcon()
        icon4.addFile(u"../../icons/svg/338.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_basedatos.setIcon(icon4)
        self.bt_basedatos.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_basedatos)

        self.bt_registrar = QPushButton(self.frame_control)
        self.bt_registrar.setObjectName(u"bt_registrar")
        self.bt_registrar.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"../../icons/svg/047.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_registrar.setIcon(icon5)
        self.bt_registrar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_registrar)

        self.bt_actualizar = QPushButton(self.frame_control)
        self.bt_actualizar.setObjectName(u"bt_actualizar")
        self.bt_actualizar.setMinimumSize(QSize(0, 40))
        icon6 = QIcon()
        icon6.addFile(u"../../icons/svg/248.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_actualizar.setIcon(icon6)
        self.bt_actualizar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_actualizar)

        self.bt_eliminar = QPushButton(self.frame_control)
        self.bt_eliminar.setObjectName(u"bt_eliminar")
        self.bt_eliminar.setMinimumSize(QSize(0, 40))
        icon7 = QIcon()
        icon7.addFile(u"../../icons/svg/030.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_eliminar.setIcon(icon7)
        self.bt_eliminar.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_eliminar)

        self.bt_ajustes = QPushButton(self.frame_control)
        self.bt_ajustes.setObjectName(u"bt_ajustes")
        self.bt_ajustes.setMinimumSize(QSize(0, 40))
        icon8 = QIcon()
        icon8.addFile(u"../../icons/svg/037.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ajustes.setIcon(icon8)
        self.bt_ajustes.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.bt_ajustes)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_paginas = QFrame(self.frame_contenido)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	background-color:#000000ff;\n"
"    color: rgb(0, 206, 151);\n"
"	border: 0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border 0px; \n"
"	font: 75 12pt \"Times New Roman\";\n"
"	color: rgb(0, 0, 0);\n"
"	borde-bottomr: 2px solid rgb(61, 61, 61);\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(61, 61, 61);\n"
"	border-radius: 15px;\n"
"    color: rgb(255, 255, 255);\n"
"	font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 206, 151);\n"
"	border-radius: 15px;\n"
"    color: rgb(0, 0, 0);\n"
"	font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	color: rgb(255, 255, 255);\n"
"	gridline-color: rgb(0, 206, 151);\n"
"	font-size: 12pt;\n"
"	color: #ffffff;\n"
"	\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(0, 206, 151);\n"
"	border: 1px solid rgb(0,0,0);\n"
"	font-size: 12px:\n"
"}\n"
"\n"
"QTableWidget QTableCornerBu"
                        "tton::section{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid rgb(0,206,151);\n"
"}")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_ajustes = QWidget()
        self.page_ajustes.setObjectName(u"page_ajustes")
        self.stackedWidget.addWidget(self.page_ajustes)
        self.page_registrar = QWidget()
        self.page_registrar.setObjectName(u"page_registrar")
        self.verticalLayout_8 = QVBoxLayout(self.page_registrar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.page_registrar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page_registrar)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_3 = QLabel(self.page_registrar)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_registrar)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_5 = QLabel(self.page_registrar)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_registrar)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.codigo_reg = QLineEdit(self.page_registrar)
        self.codigo_reg.setObjectName(u"codigo_reg")

        self.verticalLayout_6.addWidget(self.codigo_reg)

        self.nom_reg = QLineEdit(self.page_registrar)
        self.nom_reg.setObjectName(u"nom_reg")

        self.verticalLayout_6.addWidget(self.nom_reg)

        self.modelo_reg = QLineEdit(self.page_registrar)
        self.modelo_reg.setObjectName(u"modelo_reg")

        self.verticalLayout_6.addWidget(self.modelo_reg)

        self.pre_reg = QLineEdit(self.page_registrar)
        self.pre_reg.setObjectName(u"pre_reg")

        self.verticalLayout_6.addWidget(self.pre_reg)

        self.cantidad_red = QLineEdit(self.page_registrar)
        self.cantidad_red.setObjectName(u"cantidad_red")

        self.verticalLayout_6.addWidget(self.cantidad_red)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.signal_registrar = QLabel(self.page_registrar)
        self.signal_registrar.setObjectName(u"signal_registrar")
        self.signal_registrar.setMinimumSize(QSize(200, 30))
        self.signal_registrar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.signal_registrar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.bt_registrar_registrar = QPushButton(self.page_registrar)
        self.bt_registrar_registrar.setObjectName(u"bt_registrar_registrar")
        self.bt_registrar_registrar.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_5.addWidget(self.bt_registrar_registrar)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.page_registrar)
        self.page_actualizar = QWidget()
        self.page_actualizar.setObjectName(u"page_actualizar")
        self.verticalLayout_11 = QVBoxLayout(self.page_actualizar)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.page_actualizar)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.page_actualizar)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.princ_buscar = QLineEdit(self.page_actualizar)
        self.princ_buscar.setObjectName(u"princ_buscar")

        self.horizontalLayout_8.addWidget(self.princ_buscar)

        self.bt_buscar_actualizar = QPushButton(self.page_actualizar)
        self.bt_buscar_actualizar.setObjectName(u"bt_buscar_actualizar")
        self.bt_buscar_actualizar.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_8.addWidget(self.bt_buscar_actualizar)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.page_actualizar)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_9.addWidget(self.label_11)

        self.label_12 = QLabel(self.page_actualizar)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_9.addWidget(self.label_12)

        self.label_13 = QLabel(self.page_actualizar)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.label_14 = QLabel(self.page_actualizar)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_15 = QLabel(self.page_actualizar)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_9.addWidget(self.label_15)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(30)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cod_buscar = QLineEdit(self.page_actualizar)
        self.cod_buscar.setObjectName(u"cod_buscar")

        self.verticalLayout_10.addWidget(self.cod_buscar)

        self.nombre_buscar = QLineEdit(self.page_actualizar)
        self.nombre_buscar.setObjectName(u"nombre_buscar")

        self.verticalLayout_10.addWidget(self.nombre_buscar)

        self.modelo_buscar = QLineEdit(self.page_actualizar)
        self.modelo_buscar.setObjectName(u"modelo_buscar")

        self.verticalLayout_10.addWidget(self.modelo_buscar)

        self.precio_buscar = QLineEdit(self.page_actualizar)
        self.precio_buscar.setObjectName(u"precio_buscar")

        self.verticalLayout_10.addWidget(self.precio_buscar)

        self.cantidad_buscar = QLineEdit(self.page_actualizar)
        self.cantidad_buscar.setObjectName(u"cantidad_buscar")

        self.verticalLayout_10.addWidget(self.cantidad_buscar)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.signal_actualizar = QLabel(self.page_actualizar)
        self.signal_actualizar.setObjectName(u"signal_actualizar")
        self.signal_actualizar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_7.addWidget(self.signal_actualizar)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.bt_actualizar_actualizar = QPushButton(self.page_actualizar)
        self.bt_actualizar_actualizar.setObjectName(u"bt_actualizar_actualizar")
        self.bt_actualizar_actualizar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_7.addWidget(self.bt_actualizar_actualizar)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.page_actualizar)
        self.page_eliminar = QWidget()
        self.page_eliminar.setObjectName(u"page_eliminar")
        self.verticalLayout_12 = QVBoxLayout(self.page_eliminar)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_17 = QLabel(self.page_eliminar)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_17)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.page_eliminar)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_9.addWidget(self.label_18)

        self.eliminar_buscar = QLineEdit(self.page_eliminar)
        self.eliminar_buscar.setObjectName(u"eliminar_buscar")

        self.horizontalLayout_9.addWidget(self.eliminar_buscar)

        self.bt_buscar_eliminar = QPushButton(self.page_eliminar)
        self.bt_buscar_eliminar.setObjectName(u"bt_buscar_eliminar")
        self.bt_buscar_eliminar.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_9.addWidget(self.bt_buscar_eliminar)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.tabla_borrar = QTableWidget(self.page_eliminar)
        if (self.tabla_borrar.columnCount() < 6):
            self.tabla_borrar.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabla_borrar.setObjectName(u"tabla_borrar")

        self.verticalLayout_12.addWidget(self.tabla_borrar)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.signal_eliminar = QLabel(self.page_eliminar)
        self.signal_eliminar.setObjectName(u"signal_eliminar")
        self.signal_eliminar.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_10.addWidget(self.signal_eliminar)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.bt_eliminar_eliminar = QPushButton(self.page_eliminar)
        self.bt_eliminar_eliminar.setObjectName(u"bt_eliminar_eliminar")
        self.bt_eliminar_eliminar.setMinimumSize(QSize(95, 30))

        self.horizontalLayout_10.addWidget(self.bt_eliminar_eliminar)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.page_eliminar)
        self.page_datos = QWidget()
        self.page_datos.setObjectName(u"page_datos")
        self.verticalLayout_5 = QVBoxLayout(self.page_datos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.page_datos)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.tabla_productos = QTableWidget(self.page_datos)
        if (self.tabla_productos.columnCount() < 6):
            self.tabla_productos.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tabla_productos.setObjectName(u"tabla_productos")

        self.verticalLayout_5.addWidget(self.tabla_productos)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bt_refrescar = QPushButton(self.page_datos)
        self.bt_refrescar.setObjectName(u"bt_refrescar")
        self.bt_refrescar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.bt_refrescar)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_datos)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText("")
        self.bt_minimizar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_basedatos.setText(QCoreApplication.translate("MainWindow", u"BASE DE DATOS", None))
        self.bt_registrar.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.bt_actualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.bt_eliminar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.bt_ajustes.setText(QCoreApplication.translate("MainWindow", u"AJUSTES", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR PRODUCTOS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MODELO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None))
        self.signal_registrar.setText("")
        self.bt_registrar_registrar.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR PRODUCTO", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL PRODUCTO:", None))
        self.bt_buscar_actualizar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MODELO", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None))
        self.signal_actualizar.setText("")
        self.bt_actualizar_actualizar.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR PRODUCTOS", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DEL PRODUCTO:", None))
        self.bt_buscar_eliminar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem = self.tabla_borrar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_borrar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem2 = self.tabla_borrar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem3 = self.tabla_borrar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MODELO", None));
        ___qtablewidgetitem4 = self.tabla_borrar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        ___qtablewidgetitem5 = self.tabla_borrar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None));
        self.signal_eliminar.setText("")
        self.bt_eliminar_eliminar.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        ___qtablewidgetitem6 = self.tabla_productos.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tabla_productos.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem8 = self.tabla_productos.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem9 = self.tabla_productos.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"MODELO", None));
        ___qtablewidgetitem10 = self.tabla_productos.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        ___qtablewidgetitem11 = self.tabla_productos.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None));
        self.bt_refrescar.setText(QCoreApplication.translate("MainWindow", u"REFRESCAR", None))
    # retranslateUi

