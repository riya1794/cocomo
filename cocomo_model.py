# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cocomo_model.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 350)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 65, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 40, 221, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(240, 90, 110, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 120, 131, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 150, 110, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 200, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(88, 280, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 200, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setIndent(-1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 240, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setIndent(-1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 280, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setIndent(-1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Basic Cocomo Model", None))
        self.label.setText(_translate("MainWindow", "Enter the  value  of  KLOC", None))
        self.label_2.setText(_translate("MainWindow", "Model", None))
        self.radioButton.setText(_translate("MainWindow", "Oraganic", None))
        self.radioButton_2.setText(_translate("MainWindow", "Semi Detched", None))
        self.radioButton_3.setText(_translate("MainWindow", "Complex", None))
        self.label_3.setText(_translate("MainWindow", "Total Effort", None))
        self.label_4.setText(_translate("MainWindow", "Development Time", None))
        self.label_5.setText(_translate("MainWindow", "Staff Size", None))

