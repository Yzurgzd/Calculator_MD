# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_material.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calc(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 460)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/User/Downloads/calculator-icon-android-17.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 250, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 250, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 250, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 320, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 320, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 320, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 390, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_rovno = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rovno.setGeometry(QtCore.QRect(140, 390, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_rovno.setFont(font)
        self.pushButton_rovno.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_rovno.setObjectName("pushButton_rovno")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(70, 390, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("QPushButton {\n"
"    background-color: gray;   \n"
"    border: none;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 gray);\n"
"}\n"
"")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(210, 404, 70, 56))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"   background-color: #1E90FF;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                      stop: 0 #dadbde, stop: 1 #1E90FF);\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_delenie = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delenie.setGeometry(QtCore.QRect(210, 236, 70, 56))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_delenie.setFont(font)
        self.pushButton_delenie.setStyleSheet("QPushButton {\n"
"   background-color: #1E90FF;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                      stop: 0 #dadbde, stop: 1 #1E90FF);\n"
"}")
        self.pushButton_delenie.setObjectName("pushButton_delenie")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(210, 348, 70, 56))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"   background-color: #1E90FF;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                      stop: 0 #dadbde, stop: 1 #1E90FF);\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(210, 180, 70, 56))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setStyleSheet("QPushButton {\n"
"   background-color: #1E90FF;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                      stop: 0 #dadbde, stop: 1 #1E90FF);\n"
"}\n"
"\n"
"")
        self.pushButton_del.setObjectName("pushButton_del")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 270, 180))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"\n"
"  border: none;\n"
"    background-color: white;    \n"
"\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.pushButton_ymnoj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ymnoj.setGeometry(QtCore.QRect(210, 292, 70, 56))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_ymnoj.setFont(font)
        self.pushButton_ymnoj.setStyleSheet("QPushButton {\n"
"   background-color: #1E90FF;\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                      stop: 0 #dadbde, stop: 1 #1E90FF);\n"
"}")
        self.pushButton_ymnoj.setObjectName("pushButton_ymnoj")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator_MD"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_rovno.setText(_translate("MainWindow", "="))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_delenie.setText(_translate("MainWindow", "÷"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_del.setText(_translate("MainWindow", "DEL"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_ymnoj.setText(_translate("MainWindow", "×"))
