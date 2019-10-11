# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logon.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


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
"    border-image: url(:/newPrefix/images/log_background.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(50, 100, 301, 181))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.regisder_on = QtWidgets.QPushButton(self.centralwidget)
        self.regisder_on.setGeometry(QtCore.QRect(50, 400, 101, 31))
        self.regisder_on.setStyleSheet("QPushButton {\n"
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
        self.regisder_on.setObjectName("regisder_on")
        self.log_on = QtWidgets.QPushButton(self.centralwidget)
        #self.log_on.setEnabled(False)
        self.log_on.setGeometry(QtCore.QRect(300, 400, 101, 31))
        self.log_on.setStyleSheet("QPushButton {\n"
"      background-color: rgb(255, 170, 0);\n"
"      border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:disabled {\n"
"      background-color: rgb(182, 182, 182);\n"
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
        self.shi_bie = QtWidgets.QPushButton(self.centralwidget)
        # self.log_on.setEnabled(False)
        self.shi_bie.setGeometry(QtCore.QRect(550, 400, 101, 31))
        self.shi_bie.setStyleSheet("QPushButton {\n"
"      background-color: rgb(255, 170, 0);\n"
"      border-radius:10px;\n"
"\n"
"}\n"
"QPushButton:disabled {\n"
"      background-color: rgb(182, 182, 182);\n"
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
        self.shi_bie.setObjectName("log_on")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 50, 271, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.xingming = QtWidgets.QLabel(self.layoutWidget)
        self.xingming.setObjectName("xingming")
        self.gridLayout.addWidget(self.xingming, 0, 0, 1, 1)
        self.xm = QtWidgets.QLineEdit(self.layoutWidget)
        self.xm.setEnabled(False)
        self.xm.setClearButtonEnabled(False)
        self.xm.setObjectName("xm")
        self.gridLayout.addWidget(self.xm, 0, 1, 1, 1)
        self.xingbie = QtWidgets.QLabel(self.layoutWidget)
        self.xingbie.setObjectName("xingbie")
        self.gridLayout.addWidget(self.xingbie, 1, 0, 1, 1)
        self.xb = QtWidgets.QLineEdit(self.layoutWidget)
        self.xb.setEnabled(False)
        self.xb.setClearButtonEnabled(False)
        self.xb.setObjectName("xb")
        self.gridLayout.addWidget(self.xb, 1, 1, 1, 1)
        self.shenfen = QtWidgets.QLabel(self.layoutWidget)
        self.shenfen.setObjectName("shenfen")
        self.gridLayout.addWidget(self.shenfen, 2, 0, 1, 1)
        self.sfzh = QtWidgets.QLineEdit(self.layoutWidget)
        self.sfzh.setEnabled(False)
        self.sfzh.setClearButtonEnabled(False)
        self.sfzh.setObjectName("sfzh")
        self.gridLayout.addWidget(self.sfzh, 2, 1, 1, 1)
        self.rzny = QtWidgets.QLabel(self.layoutWidget)
        self.rzny.setObjectName("rzny")
        self.gridLayout.addWidget(self.rzny, 3, 0, 1, 1)
        self.rzny_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.rzny_1.setEnabled(False)
        self.rzny_1.setClearButtonEnabled(False)
        self.rzny_1.setObjectName("rzny_1")
        self.gridLayout.addWidget(self.rzny_1, 3, 1, 1, 1)
        self.lxdh = QtWidgets.QLabel(self.layoutWidget)
        self.lxdh.setObjectName("lxdh")
        self.gridLayout.addWidget(self.lxdh, 4, 0, 1, 1)
        self.lxdh_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lxdh_1.setEnabled(False)
        self.lxdh_1.setClearButtonEnabled(False)
        self.lxdh_1.setObjectName("lxdh_1")
        self.gridLayout.addWidget(self.lxdh_1, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.regisder_on.clicked.connect(MainWindow.showregister)
        self.log_on.clicked.connect(MainWindow.loadplane)
        self.shi_bie.clicked.connect(MainWindow.showshibie)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.regisder_on.setText(_translate("MainWindow", "注册账号"))
        self.log_on.setText(_translate("MainWindow", "登录"))
        self.shi_bie.setText(_translate("MainWindow", "识别"))
        self.label_3.setText(_translate("MainWindow", "录入面部："))
        self.xingming.setText(_translate("MainWindow", "姓    名："))
        self.xingbie.setText(_translate("MainWindow", "性    别："))
        self.shenfen.setText(_translate("MainWindow", "身份证号："))
        self.rzny.setText(_translate("MainWindow", "入职年月："))
        self.lxdh.setText(_translate("MainWindow", "联系电话："))
import images_log_rc
