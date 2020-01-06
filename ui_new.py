# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 20, 104, 21))
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 361, 481))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 461))
        self.groupBox.setObjectName("groupBox")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(390, 60, 391, 481))
        self.widget_2.setObjectName("widget_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 371, 461))
        self.groupBox_2.setObjectName("groupBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.pushButton.clicked.connect(lambda:self.count())
        # self.pushButton_2.clicked.connect(lambda: self.count())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
