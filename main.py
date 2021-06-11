# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'um_itemNoListView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pandas import ExcelWriter
from pandas import ExcelFile
import pandas as pd
import sys



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(694, 451)
        self.principal_frame = QtWidgets.QFrame(Form)
        self.principal_frame.setGeometry(QtCore.QRect(10, 0, 681, 451))
        self.principal_frame.setMouseTracking(True)
        self.principal_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.principal_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.principal_frame.setLineWidth(2)
        self.principal_frame.setMidLineWidth(3)
        self.principal_frame.setObjectName("principal_frame")
        self.Tlbl_titulo = QtWidgets.QLabel(self.principal_frame)
        self.Tlbl_titulo.setGeometry(QtCore.QRect(130, 20, 491, 31))
        self.Tlbl_titulo.setStyleSheet("font-size:20px;\n"
"font-weight:bold;\n"
"color:black;\n"
"text-align:center;\n"
"\n"
"")
        self.Tlbl_titulo.setObjectName("Tlbl_titulo")
        self.afd_btn = QtWidgets.QPushButton(self.principal_frame)
        self.afd_btn.setGeometry(QtCore.QRect(40, 80, 41, 51))
        self.afd_btn.setStyleSheet("border:none")
        self.afd_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hopy/images/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.afd_btn.setIcon(icon)
        self.afd_btn.setIconSize(QtCore.QSize(45, 45))
        self.afd_btn.setFlat(False)
        self.afd_btn.clicked.connect(self._afdFileSelect)
        self.afd_btn.setObjectName("afd_btn")
        self.afd_lbl = QtWidgets.QLabel(self.principal_frame)
        self.afd_lbl.setGeometry(QtCore.QRect(118, 87, 521, 41))
        self.afd_lbl.setStyleSheet("background-color:#fff;\n"
"color:blue;\n"
"font-size:12px;\n"
"text-align:center;\n"
"border:1px solid blue;\n"
"borde-radius:2px;")

        self.afd_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.afd_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.afd_lbl.setObjectName("afd_lbl")
        self.xlsx_btn = QtWidgets.QPushButton(self.principal_frame)
        self.xlsx_btn.setGeometry(QtCore.QRect(40, 172, 41, 51))
        self.xlsx_btn.setStyleSheet("border:none")
        self.xlsx_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("hopy/images/xls.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xlsx_btn.setIcon(icon1)
        self.xlsx_btn.setIconSize(QtCore.QSize(45, 45))
        self.xlsx_btn.setDefault(True)
        self.xlsx_btn.setFlat(False)
        self.xlsx_btn.setObjectName("xlsx_btn")
        self.xlsx_btn.clicked.connect(self._xlsFileSelect) #chamada de função <==>

        self.line_hr = QtWidgets.QFrame(self.principal_frame)
        self.line_hr.setGeometry(QtCore.QRect(30, 290, 611, 16))
        self.line_hr.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_hr.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_hr.setObjectName("line_hr")

        self.alerta_lbl = QtWidgets.QLabel(self.principal_frame)
        self.alerta_lbl.setGeometry(QtCore.QRect(30, 350, 431, 51))
        self.alerta_lbl.setStyleSheet("font-size:12px;\n"
"font-weight:bold;\n"
"color:red;\n"
"padding:10px;\n"
"")
        self.alerta_lbl.setObjectName("alerta_lbl")

        self.progressBar = QtWidgets.QProgressBar(self.principal_frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 320, 631, 23))
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setStyleSheet("text-align:center;\n"
"font-size:14px;\n"
"color:blue;\n"
"font-weight:bold;\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")

        self.start_btn = QtWidgets.QPushButton(self.principal_frame)
        self.start_btn.setGeometry(QtCore.QRect(480, 360, 75, 23))
        self.start_btn.setStyleSheet("border-radius:4px;\n"
"border:none;\n"
"color:white;\n"
"background-color:green;\n"
"font-weight:bold;\n"
"font-size:12px;\n"
"text-align:center")
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self._start)
        self.cancel_btn = QtWidgets.QPushButton(self.principal_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(580, 360, 75, 23))
        self.cancel_btn.setStyleSheet("border-radius:4px;\n"
"border:none;\n"
"color:white;\n"
"background-color:red;\n"
"font-weight:bold;\n"
"font-size:12px;\n"
"text-align:center")

        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self._cancel)

        self.line_2 = QtWidgets.QFrame(self.principal_frame)
        self.line_2.setGeometry(QtCore.QRect(560, 350, 16, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.xlsx_listWidget = QtWidgets.QListWidget(self.principal_frame)
        self.xlsx_listWidget.setGeometry(QtCore.QRect(117, 150, 521, 91))
        self.xlsx_listWidget.setStyleSheet("text-align:center;\n"
"background-color:#fff;\n"
"padding-left:10px;\n"
"color:blue;\n"
"font-size:12px;\n"
"text-align:center;\n"
"border:1px solid blue;\n"
"borde-radius:2px;")

        self.xlsx_listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.xlsx_listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.xlsx_listWidget.setObjectName("xlsx_listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.comboBox = QtWidgets.QComboBox(self.principal_frame)
        self.comboBox.setGeometry(QtCore.QRect(430, 260, 101, 21))
        self.comboBox.setStyleSheet("text-align:center;\n"
"background-color:#fff;\n"
"color:blue;\n"
"font-size:14px;\n"
"border:1px solid;\n"
"")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(11, "Dezembro")
       
        self.label = QtWidgets.QLabel(self.principal_frame)
        self.label.setGeometry(QtCore.QRect(190, 254, 201, 31))
        self.label.setStyleSheet("font-size:14px;\n"
"font-weight:bold;\n"
"color:rgb(0, 0, 0);\n"
"text-align:center;\n"
"")
        self.label.setObjectName("label")
        self.progressBar.raise_()
        self.Tlbl_titulo.raise_()
        self.afd_btn.raise_()
        self.afd_lbl.raise_()
        self.xlsx_btn.raise_()
        self.line_hr.raise_()
        self.alerta_lbl.raise_()
        self.start_btn.raise_()
        self.cancel_btn.raise_()
        self.line_2.raise_()
        self.xlsx_listWidget.raise_()
        self.comboBox.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Tlbl_titulo.setText(_translate("Form", "Home Office auxiliar de ajuste de marcação  ®"))
        self.afd_lbl.setText(_translate("Form", "Selecione o arquivo no formato AFD  "))
        self.alerta_lbl.setText(_translate("Form", "Por favor aguarde a barra de progresso atingir 100%"))
        self.progressBar.setFormat(_translate("Form", "%p%"))
        self.start_btn.setText(_translate("Form", "INICIAR"))
        self.cancel_btn.setText(_translate("Form", "SAIR"))

       
        self.comboBox.setItemText(0, _translate("Form", "Janeiro"))
        self.comboBox.setItemText(1, _translate("Form", "Fevereiro"))
        self.comboBox.setItemText(2, _translate("Form", "Março"))
        self.comboBox.setItemText(3, _translate("Form", "Abril"))
        self.comboBox.setItemText(4, _translate("Form", "Maio"))
        self.comboBox.setItemText(5, _translate("Form", "Junho"))
        self.comboBox.setItemText(6, _translate("Form", "Julho"))
        self.comboBox.setItemText(7, _translate("Form", "Agosto"))
        self.comboBox.setItemText(8, _translate("Form", "Setembro"))
        self.comboBox.setItemText(9, _translate("Form", "Outubro"))
        self.comboBox.setItemText(10, _translate("Form","Novembro"))
        self.label.setText(_translate("Form", "Selecione o mês de referencia:"))

    def _afdFileSelect(self):
        self.afd_file = QFileDialog.getOpenFileName(self.afd_btn,filter="txt Files (*.txt)")
        print(self.afd_file[0])
        self.afd_lbl.setText(self.afd_file[0])
        
        text=open(self.afd_file[0]).readlines()
        final_line = len(text)-1
        print(text[final_line])
        
    def _readExcelFiles(self,xlsxList):
            df = pd.read_excel(xlsxList,sheet_name = self.comboBox.currentText(),skiprows = range(0, 11))
            print("Column headings:")
            print(df.columns.values)
      
    def _xlsFileSelect(self):
        xlx_file = QFileDialog.getOpenFileNames( self.xlsx_btn,filter="Excel Files (*.xlsx)")
        xlx_file_list = xlx_file[0]  
        
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.xlsx_listWidget.isSortingEnabled()
        for x in range(len(xlx_file_list)):
                item = QtWidgets.QListWidgetItem()
                self.xlsx_listWidget.addItem(item)
                item = self.xlsx_listWidget.item(x)
                list_tem  = xlx_file_list[x].split("/")
                item.setText(_translate("Form",list_tem[len(list_tem)-1]))
                print(xlx_file_list[x])
        self.xlsx_listWidget.setSortingEnabled(__sortingEnabled)
        self._readExcelFiles(xlx_file_list[0])
                       

    def _cancel(self):
        sys.exit(app.exec_())

    def _start(self):
            #fazer a barra encher 
            print(self.comboBox.currentText(), self.comboBox.currentIndex())
            for x in range(101):
                self.progressBar.setProperty("value", x)
         
            

               


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
