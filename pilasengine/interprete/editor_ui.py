# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilasengine/interprete/editor.ui'
#
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName(_fromUtf8("Editor"))
        Editor.resize(638, 573)
        Editor.setStyleSheet(_fromUtf8(""))
        self.layoutWidget = QtGui.QWidget(Editor)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 358, 289))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.vertical_layout = QtGui.QVBoxLayout(self.layoutWidget)
        self.vertical_layout.setMargin(0)
        self.vertical_layout.setObjectName(_fromUtf8("vertical_layout"))
        self.hbox_buttons = QtGui.QHBoxLayout()
        self.hbox_buttons.setObjectName(_fromUtf8("hbox_buttons"))
        self.boton_abrir = QtGui.QPushButton(self.layoutWidget)
        self.boton_abrir.setEnabled(True)
        self.boton_abrir.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_abrir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_abrir.setFlat(True)
        self.boton_abrir.setObjectName(_fromUtf8("boton_abrir"))
        self.hbox_buttons.addWidget(self.boton_abrir)
        self.boton_guardar = QtGui.QPushButton(self.layoutWidget)
        self.boton_guardar.setEnabled(True)
        self.boton_guardar.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_guardar.setFlat(True)
        self.boton_guardar.setObjectName(_fromUtf8("boton_guardar"))
        self.hbox_buttons.addWidget(self.boton_guardar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hbox_buttons.addItem(spacerItem)
        self.boton_ejecutar = QtGui.QPushButton(self.layoutWidget)
        self.boton_ejecutar.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_ejecutar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_ejecutar.setFlat(True)
        self.boton_ejecutar.setObjectName(_fromUtf8("boton_ejecutar"))
        self.hbox_buttons.addWidget(self.boton_ejecutar)
        self.boton_pausar = QtGui.QPushButton(self.layoutWidget)
        self.boton_pausar.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_pausar.setCheckable(True)
        self.boton_pausar.setFlat(True)
        self.boton_pausar.setObjectName(_fromUtf8("boton_pausar"))
        self.hbox_buttons.addWidget(self.boton_pausar)
        self.boton_siguiente = QtGui.QPushButton(self.layoutWidget)
        self.boton_siguiente.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_siguiente.setFlat(True)
        self.boton_siguiente.setObjectName(_fromUtf8("boton_siguiente"))
        self.hbox_buttons.addWidget(self.boton_siguiente)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hbox_buttons.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setLineWidth(0)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.hbox_buttons.addWidget(self.label)
        self.vertical_layout.addLayout(self.hbox_buttons)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setMargin(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.hbox_editor = QtGui.QHBoxLayout()
        self.hbox_editor.setObjectName(_fromUtf8("hbox_editor"))
        self.gridLayout_2.addLayout(self.hbox_editor, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setMargin(5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lista_actores = QtGui.QListWidget(self.tab_2)
        self.lista_actores.setFrameShape(QtGui.QFrame.Box)
        self.lista_actores.setObjectName(_fromUtf8("lista_actores"))
        self.gridLayout_3.addWidget(self.lista_actores, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.vertical_layout.addWidget(self.tabWidget)
        self.consejo = QtGui.QLabel(self.layoutWidget)
        self.consejo.setFrameShape(QtGui.QFrame.NoFrame)
        self.consejo.setFrameShadow(QtGui.QFrame.Plain)
        self.consejo.setLineWidth(0)
        self.consejo.setMidLineWidth(0)
        self.consejo.setText(_fromUtf8(""))
        self.consejo.setObjectName(_fromUtf8("consejo"))
        self.vertical_layout.addWidget(self.consejo)

        self.retranslateUi(Editor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        Editor.setWindowTitle(_translate("Editor", "Form", None))
        self.boton_abrir.setToolTip(_translate("Editor", "Abrir archivo", None))
        self.boton_abrir.setText(_translate("Editor", "A", None))
        self.boton_guardar.setToolTip(_translate("Editor", "Guardar código en un archivo", None))
        self.boton_guardar.setText(_translate("Editor", "G", None))
        self.boton_ejecutar.setToolTip(_translate("Editor", "Ejecutar el código actual (F5 o CTRL+R)", None))
        self.boton_ejecutar.setText(_translate("Editor", "E", None))
        self.boton_pausar.setText(_translate("Editor", "P", None))
        self.boton_siguiente.setText(_translate("Editor", "S", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Editor", "Editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Editor", "Actores", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Editor = QtGui.QWidget()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())

