# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pdf.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.unirPDF = QtWidgets.QGroupBox(self.centralwidget)
        self.unirPDF.setObjectName("unirPDF")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.unirPDF)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.unir6 = QtWidgets.QLineEdit(self.unirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unir6.sizePolicy().hasHeightForWidth())
        self.unir6.setSizePolicy(sizePolicy)
        self.unir6.setMinimumSize(QtCore.QSize(0, 15))
        self.unir6.setObjectName("unir6")
        self.gridLayout_2.addWidget(self.unir6, 5, 0, 1, 1)
        self.unir3 = QtWidgets.QLineEdit(self.unirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unir3.sizePolicy().hasHeightForWidth())
        self.unir3.setSizePolicy(sizePolicy)
        self.unir3.setMinimumSize(QtCore.QSize(0, 15))
        self.unir3.setObjectName("unir3")
        self.gridLayout_2.addWidget(self.unir3, 2, 0, 1, 1)
        self.unir2 = QtWidgets.QLineEdit(self.unirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unir2.sizePolicy().hasHeightForWidth())
        self.unir2.setSizePolicy(sizePolicy)
        self.unir2.setMinimumSize(QtCore.QSize(0, 15))
        self.unir2.setObjectName("unir2")
        self.gridLayout_2.addWidget(self.unir2, 1, 0, 1, 1)
        self.unir4 = QtWidgets.QLineEdit(self.unirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unir4.sizePolicy().hasHeightForWidth())
        self.unir4.setSizePolicy(sizePolicy)
        self.unir4.setMinimumSize(QtCore.QSize(0, 15))
        self.unir4.setObjectName("unir4")
        self.gridLayout_2.addWidget(self.unir4, 3, 0, 1, 1)
        self.unir1 = QtWidgets.QLineEdit(self.unirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unir1.sizePolicy().hasHeightForWidth())
        self.unir1.setSizePolicy(sizePolicy)
        self.unir1.setMinimumSize(QtCore.QSize(0, 15))
        self.unir1.setObjectName("unir1")
        self.gridLayout_2.addWidget(self.unir1, 0, 0, 1, 1)
        self.unir5 = QtWidgets.QLineEdit(self.unirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unir5.sizePolicy().hasHeightForWidth())
        self.unir5.setSizePolicy(sizePolicy)
        self.unir5.setMinimumSize(QtCore.QSize(0, 15))
        self.unir5.setObjectName("unir5")
        self.gridLayout_2.addWidget(self.unir5, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.unirPDF, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnAddArquivo = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddArquivo.sizePolicy().hasHeightForWidth())
        self.btnAddArquivo.setSizePolicy(sizePolicy)
        self.btnAddArquivo.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddArquivo.setFont(font)
        self.btnAddArquivo.setObjectName("btnAddArquivo")
        self.gridLayout_4.addWidget(self.btnAddArquivo, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 7, 0, 1, 1)
        self.checkBoxDelUnir = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.checkBoxDelUnir.setFont(font)
        self.checkBoxDelUnir.setObjectName("checkBoxDelUnir")
        self.gridLayout_4.addWidget(self.checkBoxDelUnir, 6, 0, 1, 1)
        self.saida = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saida.sizePolicy().hasHeightForWidth())
        self.saida.setSizePolicy(sizePolicy)
        self.saida.setMinimumSize(QtCore.QSize(0, 0))
        self.saida.setObjectName("saida")
        self.gridLayout_4.addWidget(self.saida, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 2, 0, 1, 1)
        self.btnUnir = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUnir.sizePolicy().hasHeightForWidth())
        self.btnUnir.setSizePolicy(sizePolicy)
        self.btnUnir.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnUnir.setFont(font)
        self.btnUnir.setObjectName("btnUnir")
        self.gridLayout_4.addWidget(self.btnUnir, 8, 0, 1, 1)
        self.btnSaida = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnSaida.setFont(font)
        self.btnSaida.setObjectName("btnSaida")
        self.gridLayout_4.addWidget(self.btnSaida, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 2, 1, 1)
        self.dividirPDF = QtWidgets.QGroupBox(self.centralwidget)
        self.dividirPDF.setObjectName("dividirPDF")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dividirPDF)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.dividirPDF)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.checkBoxDelDividir = QtWidgets.QCheckBox(self.dividirPDF)
        self.checkBoxDelDividir.setObjectName("checkBoxDelDividir")
        self.gridLayout_3.addWidget(self.checkBoxDelDividir, 1, 0, 1, 1)
        self.btnEscolheArquivo = QtWidgets.QPushButton(self.dividirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEscolheArquivo.sizePolicy().hasHeightForWidth())
        self.btnEscolheArquivo.setSizePolicy(sizePolicy)
        self.btnEscolheArquivo.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnEscolheArquivo.setFont(font)
        self.btnEscolheArquivo.setObjectName("btnEscolheArquivo")
        self.gridLayout_3.addWidget(self.btnEscolheArquivo, 2, 0, 1, 1)
        self.btnUnir_ = QtWidgets.QPushButton(self.dividirPDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUnir_.sizePolicy().hasHeightForWidth())
        self.btnUnir_.setSizePolicy(sizePolicy)
        self.btnUnir_.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnUnir_.setFont(font)
        self.btnUnir_.setObjectName("btnUnir_")
        self.gridLayout_3.addWidget(self.btnUnir_, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.dividirPDF, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Unir"))
        self.unirPDF.setTitle(_translate("MainWindow", "Unir PDF\'s:"))
        self.btnAddArquivo.setText(_translate("MainWindow", "Adicionar\n"
" Arquivo"))
        self.checkBoxDelUnir.setText(_translate("MainWindow", "Apagar Originais"))
        self.btnUnir.setText(_translate("MainWindow", "UNIR!"))
        self.btnSaida.setText(_translate("MainWindow", "Pasta de saída"))
        self.dividirPDF.setTitle(_translate("MainWindow", "Dividir PDF:"))
        self.checkBoxDelDividir.setText(_translate("MainWindow", "Apagar arquivo original"))
        self.btnEscolheArquivo.setText(_translate("MainWindow", "Escolher Arquivo"))
        self.btnUnir_.setText(_translate("MainWindow", "DIVIDIR!"))