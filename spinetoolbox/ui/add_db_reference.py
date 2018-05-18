#############################################################################
# Copyright (C) 2017 - 2018 VTT Technical Research Centre of Finland
#
# This file is part of Spine Toolbox.
#
# Spine Toolbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../spinetoolbox/ui/add_db_reference.ui'
#
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(300, 254)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_dialect = QtWidgets.QComboBox(Form)
        self.comboBox_dialect.setObjectName("comboBox_dialect")
        self.verticalLayout.addWidget(self.comboBox_dialect)
        self.lineEdit_host = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_host.setSizePolicy(sizePolicy)
        self.lineEdit_host.setMinimumSize(QtCore.QSize(220, 20))
        self.lineEdit_host.setMaximumSize(QtCore.QSize(5000, 20))
        self.lineEdit_host.setClearButtonEnabled(True)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.verticalLayout.addWidget(self.lineEdit_host)
        self.lineEdit_port = QtWidgets.QLineEdit(Form)
        self.lineEdit_port.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.verticalLayout.addWidget(self.lineEdit_port)
        self.lineEdit_database = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_database.sizePolicy().hasHeightForWidth())
        self.lineEdit_database.setSizePolicy(sizePolicy)
        self.lineEdit_database.setMinimumSize(QtCore.QSize(220, 20))
        self.lineEdit_database.setMaximumSize(QtCore.QSize(5000, 20))
        self.lineEdit_database.setClearButtonEnabled(True)
        self.lineEdit_database.setObjectName("lineEdit_database")
        self.verticalLayout.addWidget(self.lineEdit_database)
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_username.sizePolicy().hasHeightForWidth())
        self.lineEdit_username.setSizePolicy(sizePolicy)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(220, 20))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(5000, 20))
        self.lineEdit_username.setClearButtonEnabled(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(220, 20))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(5000, 20))
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        spacerItem = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 6, 0, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_ok = QtWidgets.QPushButton(Form)
        self.pushButton_ok.setDefault(True)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setDefault(True)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_statusbar_placeholder = QtWidgets.QHBoxLayout()
        self.horizontalLayout_statusbar_placeholder.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_statusbar_placeholder.setObjectName("horizontalLayout_statusbar_placeholder")
        self.widget_invisible_dummy = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_invisible_dummy.sizePolicy().hasHeightForWidth())
        self.widget_invisible_dummy.setSizePolicy(sizePolicy)
        self.widget_invisible_dummy.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_invisible_dummy.setMaximumSize(QtCore.QSize(0, 20))
        self.widget_invisible_dummy.setObjectName("widget_invisible_dummy")
        self.horizontalLayout_statusbar_placeholder.addWidget(self.widget_invisible_dummy)
        self.verticalLayout_2.addLayout(self.horizontalLayout_statusbar_placeholder)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox_dialect, self.lineEdit_host)
        Form.setTabOrder(self.lineEdit_host, self.lineEdit_port)
        Form.setTabOrder(self.lineEdit_port, self.lineEdit_database)
        Form.setTabOrder(self.lineEdit_database, self.lineEdit_username)
        Form.setTabOrder(self.lineEdit_username, self.lineEdit_password)
        Form.setTabOrder(self.lineEdit_password, self.pushButton_ok)
        Form.setTabOrder(self.pushButton_ok, self.pushButton_cancel)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Add Database Reference", None, -1))
        self.lineEdit_host.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Host (required)</p></body></html>", None, -1))
        self.lineEdit_host.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Type host name here...", None, -1))
        self.lineEdit_port.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Port (optional)</p></body></html>", None, -1))
        self.lineEdit_port.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Type port number here...", None, -1))
        self.lineEdit_database.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Database (required)</p></body></html>", None, -1))
        self.lineEdit_database.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Type database name here...", None, -1))
        self.lineEdit_username.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Username (optional)</p></body></html>", None, -1))
        self.lineEdit_username.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Type username here...", None, -1))
        self.lineEdit_password.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Password (optional)</p></body></html>", None, -1))
        self.lineEdit_password.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Type password here...", None, -1))
        self.pushButton_ok.setText(QtWidgets.QApplication.translate("Form", "Ok", None, -1))
        self.pushButton_cancel.setText(QtWidgets.QApplication.translate("Form", "Cancel", None, -1))
