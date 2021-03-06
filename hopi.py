# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hope.ui'
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
import sys





class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        
        self.xlx_file = ""
        self.afd_file = ""
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(60, 200, 531, 23))
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setStyleSheet("text-align:center;")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setGeometry(QtCore.QRect(420, 250, 75, 23))
        self.start_button.setStyleSheet("border-radius:4px;border:none;color:white;background-color:green;font-weight:bold;font-size:12px;text-align:center")
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.satrt_process) #chamada de função <==>
        
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(510, 250, 75, 23))
        self.cancel_button.setStyleSheet("border-radius:4px;border:none;color:white;background-color:red;font-weight:bold;font-size:12px;text-align:center")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(self.cancel) #chamada de função <==>
        
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 30, 571, 271))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("backgound-color:blue;padding:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.AFD_Select_button = QtWidgets.QPushButton(self.frame)
        self.AFD_Select_button.setGeometry(QtCore.QRect(20, 33, 51, 51))
        self.AFD_Select_button.setStyleSheet("border:none;")
        self.AFD_Select_button.setText("")
        self.AFD_Select_button.clicked.connect(self._afdFileSelect) #chamada de função <==>
        self.cancel_button.clicked.connect(self.cancel) 
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hopy/images/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AFD_Select_button.setIcon(icon)
        self.AFD_Select_button.setIconSize(QtCore.QSize(36, 36))
        self.AFD_Select_button.setObjectName("AFD_Select_button")
        self.xlx_select_button = QtWidgets.QPushButton(self.frame)
        self.xlx_select_button.setEnabled(True)
        self.xlx_select_button.setGeometry(QtCore.QRect(26, 93, 41, 51))
        self.xlx_select_button.setStyleSheet("border:none;border:1px solir green;border-radius:4px;")
        self.xlx_select_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("hopy/images/xls.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xlx_select_button.setIcon(icon1)
        self.xlx_select_button.setIconSize(QtCore.QSize(36, 36))
        self.xlx_select_button.setObjectName("xlx_select_files")
        self.xlx_select_button.clicked.connect(self._xlsFileSelect) #chamada de função <==>
        self.lbl_load_notify = QtWidgets.QLabel(self.frame)
        self.lbl_load_notify.setGeometry(QtCore.QRect(20, 210, 301, 41))
        self.lbl_load_notify.setStyleSheet("font-size:12px;font-weight:bold;color:red;padding:10px;")
        self.lbl_load_notify.setObjectName("lbl_load_notify")
        self.lbl_file_selection_field = QtWidgets.QLabel(self.frame)
        self.lbl_file_selection_field.setGeometry(QtCore.QRect(80, 40, 471, 41))
        self.lbl_file_selection_field.setAutoFillBackground(False)
        self.lbl_file_selection_field.setStyleSheet("background-color:#fff;color:blue;font-size:10px;text-align:center;border:1px solid blue;borde-radius:2px;")
        self.lbl_file_selection_field.setTextFormat(QtCore.Qt.RichText)
        self.lbl_file_selection_field.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_file_selection_field.setObjectName("lbl_file_selection_field")
        self.lbl_xlx_slected_file = QtWidgets.QLabel(self.frame)
        self.lbl_xlx_slected_file.setGeometry(QtCore.QRect(80, 100, 471, 41))
        self.lbl_xlx_slected_file.setStyleSheet("background-color:#fff;color:blue;font-size:12px;text-align:center;border:1px solid blue;borde-radius:2px;")
        self.lbl_xlx_slected_file.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_xlx_slected_file.setObjectName("lbl_xlx_slected_file")
        
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 150, 551, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 192, 551, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(447, 221, 30, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 160, 20, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(551, 160, 20, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(10, 13, 551, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(0, 20, 20, 141))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(551, 21, 20, 141))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setEnabled(True)
        self.line_9.setGeometry(QtCore.QRect(10, 246, 551, 20))
        self.line_9.setStyleSheet("border-color:black;")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(-9, 0, 20, 271))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(0, -7, 571, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.verticalScrollBar.setGeometry(QtCore.QRect(528, 105, 20, 31))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(600, 30, 20, 271))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")

 

        self.line_13 = QtWidgets.QFrame(Dialog)
        self.line_13.setGeometry(QtCore.QRect(40, 293, 571, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 261, 16))
        self.label.setStyleSheet("font-weight:bold;color:black;text-align:center;")
        self.label.setObjectName("label")
        self.frame.raise_()
        self.progressBar.raise_()
        self.start_button.raise_()
        self.cancel_button.raise_()
        self.line_11.raise_()
        self.line_13.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HOPI"))
        self.start_button.setText(_translate("Dialog", "INICIO"))
        self.cancel_button.setText(_translate("Dialog", "CANCELA"))
        self.lbl_load_notify.setText(_translate("Dialog", "Por Favor aguarde ate completar 100%"))
        self.lbl_file_selection_field.setText(_translate("Dialog", "Selecio e o arquivo txt em padrão AFD"))
        self.lbl_xlx_slected_file.setText(_translate("Dialog", "Selecione os arquivos xlx"))
        self.label.setText(_translate("Dialog", "Home Office auxiliar de ajuste de marcação  ®"))

    def _afdFileSelect(self,Dialog):
        self.afd_file = QFileDialog.getOpenFileName(self.AFD_Select_button,filter="txt Files (*.txt)")
        print(self.afd_file[0])
        self.lbl_file_selection_field.setText(self.afd_file[0])
        
        text=open(self.afd_file[0]).readlines()
        final_line = len(text)-1
        print(text[final_line])

    def _xlsFileSelect(self):
        xlx_file = QFileDialog.getOpenFileNames(self.AFD_Select_button,filter="Excel Files (*.xlsx)")
        xlx_file_list = xlx_file[0]
        xls_files =""
        for xlx in xlx_file_list:
            xls_files+=xlx+'\n'
        self.lbl_xlx_slected_file.setText("{}".format(xls_files))
        print(xls_files)

    def satrt_process(self):
        print(self.afd_file[0])


    def cancel(self):
        sys.exit(app.exec_())



     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
