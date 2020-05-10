# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(962, 623)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(17, 60, 931, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.add_name.setObjectName("add_name")
        self.horizontalLayout.addWidget(self.add_name)
        self.url_ipt = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.url_ipt.setObjectName("url_ipt")
        self.horizontalLayout.addWidget(self.url_ipt)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(18, 120, 931, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save_url = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.save_url.setObjectName("save_url")
        self.horizontalLayout_2.addWidget(self.save_url)
        self.line_url_save = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.line_url_save.setObjectName("line_url_save")
        self.horizontalLayout_2.addWidget(self.line_url_save)
        self.button_out = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_out.setObjectName("button_out")
        self.horizontalLayout_2.addWidget(self.button_out)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 170, 931, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.show_window = QtWidgets.QGraphicsView(Form)
        self.show_window.setGeometry(QtCore.QRect(20, 210, 931, 401))
        self.show_window.setObjectName("show_window")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(17, 10, 931, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.retranslateUi(Form)
        self.button_out.clicked.connect(Form.run)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_name.setText(_translate("Form", "添加网址："))
        self.save_url.setText(_translate("Form", "保存路径:"))
        self.button_out.setText(_translate("Form", "导出图片"))
        self.label.setText(_translate("Form", "导出进度："))
        self.label_2.setText(_translate("Form", "设置cookie:"))
