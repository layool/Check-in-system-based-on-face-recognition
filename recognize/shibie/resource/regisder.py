# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regisder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import already
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 495)
        MainWindow.setMinimumSize(QtCore.QSize(750, 495))
        MainWindow.setMaximumSize(QtCore.QSize(750, 495))
        MainWindow.setStyleSheet("\n"
"QWidget#centralwidget{\n"
"     border-image: url(:/register/images/regisder_background.jpg);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(750, 495))
        self.centralwidget.setMaximumSize(QtCore.QSize(750, 495))
        self.centralwidget.setObjectName("centralwidget")
        self.lrlb = QtWidgets.QLabel(self.centralwidget)
        self.lrlb.setGeometry(QtCore.QRect(340, 100, 71, 21))
        self.lrlb.setObjectName("lrlb")
        self.qr = QtWidgets.QPushButton(self.centralwidget)
        self.qr.setEnabled(False)
        self.qr.setGeometry(QtCore.QRect(440, 320, 100, 40))
        self.qr.setStyleSheet("QPushButton {\n"
"      background-color: rgb(255, 170, 0);\n"
"      border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:disabled{\n"
"      background-color: rgb(167, 167, 167);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"      background-color:rgb(255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"      background-color:rgb(214, 71, 0);\n"
"\n"
"}")
        self.qr.setAutoDefault(False)
        self.qr.setDefault(False)
        self.qr.setObjectName("qr")
        self.chongzhi = QtWidgets.QPushButton(self.centralwidget)
        self.chongzhi.setGeometry(QtCore.QRect(580, 320, 100, 40))
        self.chongzhi.setStyleSheet("QPushButton {\n"
"      background-color: rgb(255, 170, 0);\n"
"      border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"      background-color:rgb(255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"      background-color:rgb(214, 71, 0);\n"
"\n"
"}")
        self.chongzhi.setObjectName("chongzhi")
        self.tc = QtWidgets.QPushButton(self.centralwidget)
        self.tc.setEnabled(True)
        self.tc.setGeometry(QtCore.QRect(440, 380, 100, 40))
        self.tc.setStyleSheet("QPushButton {\n"
"      background-color: rgb(255, 170, 0);\n"
"      border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"      background-color:rgb(255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"      background-color:rgb(214, 71, 0);\n"
"\n"
"}")
        self.tc.setObjectName("tc")
        self.sk = QtWidgets.QPushButton(self.centralwidget)
        self.sk.setGeometry(QtCore.QRect(580, 380, 100, 40))
        self.sk.setStyleSheet("QPushButton {\n"
"      background-color: rgb(255, 170, 0);\n"
"      border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"      background-color:rgb(255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"      background-color:rgb(214, 71, 0);\n"
"\n"
"}")
        self.sk.setObjectName("shanku")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 271, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.xingming = QtWidgets.QLabel(self.layoutWidget)
        self.xingming.setObjectName("xingming")
        self.gridLayout.addWidget(self.xingming, 0, 0, 1, 1)
        self.xm = QtWidgets.QLineEdit(self.layoutWidget)
        self.xm.setClearButtonEnabled(False)
        self.xm.setObjectName("xm")
        self.gridLayout.addWidget(self.xm, 0, 1, 1, 1)
        self.xingbie = QtWidgets.QLabel(self.layoutWidget)
        self.xingbie.setObjectName("xingbie")
        self.gridLayout.addWidget(self.xingbie, 1, 0, 1, 1)
        self.xb = QtWidgets.QLineEdit(self.layoutWidget)
        self.xb.setClearButtonEnabled(False)
        self.xb.setObjectName("xb")
        self.gridLayout.addWidget(self.xb, 1, 1, 1, 1)
        self.shenfen = QtWidgets.QLabel(self.layoutWidget)
        self.shenfen.setObjectName("shenfen")
        self.gridLayout.addWidget(self.shenfen, 2, 0, 1, 1)
        self.sfzh = QtWidgets.QLineEdit(self.layoutWidget)
        self.sfzh.setClearButtonEnabled(False)
        self.sfzh.setObjectName("sfzh")
        self.gridLayout.addWidget(self.sfzh, 2, 1, 1, 1)
        self.rzny = QtWidgets.QLabel(self.layoutWidget)
        self.rzny.setObjectName("rzny")
        self.gridLayout.addWidget(self.rzny, 3, 0, 1, 1)
        self.rzny_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.rzny_1.setClearButtonEnabled(False)
        self.rzny_1.setObjectName("rzny_1")
        self.gridLayout.addWidget(self.rzny_1, 3, 1, 1, 1)
        self.lxdh = QtWidgets.QLabel(self.layoutWidget)
        self.lxdh.setObjectName("lxdh")
        self.gridLayout.addWidget(self.lxdh, 4, 0, 1, 1)
        self.lxdh_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lxdh_1.setClearButtonEnabled(False)
        self.lxdh_1.setObjectName("lxdh_1")
        self.gridLayout.addWidget(self.lxdh_1, 4, 1, 1, 1)
        self.lrmb = QtWidgets.QLabel(self.centralwidget)
        self.lrmb.setGeometry(QtCore.QRect(400, 110, 311, 191))
        self.lrmb.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.lrmb.setText("")
        self.lrmb.setObjectName("lrmb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chongzhi.clicked.connect(MainWindow.reset)
        self.qr.clicked.connect(MainWindow.queren)
        self.xm.textChanged['QString'].connect(MainWindow.enableregisder)
        self.xb.textChanged['QString'].connect(MainWindow.enableregisder)
        self.sfzh.textChanged['QString'].connect(MainWindow.enableregisder)
        self.lxdh_1.textChanged['QString'].connect(MainWindow.enableregisder)
        self.rzny_1.textChanged['QString'].connect(MainWindow.enableregisder)
        #self.tc.clicked.connect(MainWindow.tuichu)
        #self.tc.clicked.connect(MainWindow.daoku)
        fff=already.ProgressBar()
        self.tc.clicked.connect(lambda:fff.show())
        self.sk.clicked.connect(MainWindow.shanku)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lrlb.setText(_translate("MainWindow", "录入面部："))
        self.qr.setText(_translate("MainWindow", "确认"))
        self.chongzhi.setText(_translate("MainWindow", "重置"))
        self.tc.setText(_translate("MainWindow", "导库"))
        self.sk.setText(_translate("MainWindow", "删库"))
        self.xingming.setText(_translate("MainWindow", "姓    名："))
        self.xingbie.setText(_translate("MainWindow", "性    别："))
        self.shenfen.setText(_translate("MainWindow", "身份证号："))
        self.rzny.setText(_translate("MainWindow", "入职年月："))
        self.lxdh.setText(_translate("MainWindow", "联系电话："))
import images_rc
