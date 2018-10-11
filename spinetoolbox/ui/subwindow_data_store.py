######################################################################################################################
# Copyright (C) 2017 - 2018 Spine project consortium
# This file is part of Spine Toolbox.
# Spine Toolbox is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option)
# any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General
# Public License for more details. You should have received a copy of the GNU Lesser General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
######################################################################################################################

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../spinetoolbox/ui/subwindow_data_store.ui',
# licensing of '../spinetoolbox/ui/subwindow_data_store.ui' applies.
#
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(303, 402)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(200, 275))
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Form.setToolTip("")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setContentsMargins(4, -1, 4, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_name = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QtCore.QSize(0, 18))
        self.label_name.setMaximumSize(QtCore.QSize(16777215, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("background-color: rgb(0,255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setWordWrap(True)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_3.addWidget(self.label_name)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_dialect = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_dialect.sizePolicy().hasHeightForWidth())
        self.comboBox_dialect.setSizePolicy(sizePolicy)
        self.comboBox_dialect.setObjectName("comboBox_dialect")
        self.horizontalLayout_4.addWidget(self.comboBox_dialect)
        self.toolButton_spine = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_spine.sizePolicy().hasHeightForWidth())
        self.toolButton_spine.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Spine_db_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_spine.setIcon(icon)
        self.toolButton_spine.setObjectName("toolButton_spine")
        self.horizontalLayout_4.addWidget(self.toolButton_spine)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 2)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(5000, 5000))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 6, 1, 1, 2)
        self.comboBox_dsn = QtWidgets.QComboBox(Form)
        self.comboBox_dsn.setEnabled(False)
        self.comboBox_dsn.setObjectName("comboBox_dsn")
        self.gridLayout.addWidget(self.comboBox_dsn, 1, 1, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_host = QtWidgets.QLineEdit(Form)
        self.lineEdit_host.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_host.setSizePolicy(sizePolicy)
        self.lineEdit_host.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_host.setMaximumSize(QtCore.QSize(5000, 5000))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_host.setFont(font)
        self.lineEdit_host.setPlaceholderText("")
        self.lineEdit_host.setClearButtonEnabled(True)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.horizontalLayout_2.addWidget(self.lineEdit_host)
        self.label_port = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_port.sizePolicy().hasHeightForWidth())
        self.label_port.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_2.addWidget(self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(Form)
        self.lineEdit_port.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_port.setSizePolicy(sizePolicy)
        self.lineEdit_port.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_port.setMaximumSize(QtCore.QSize(80, 5000))
        self.lineEdit_port.setPlaceholderText("")
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_2.addWidget(self.lineEdit_port)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 2)
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_username.sizePolicy().hasHeightForWidth())
        self.lineEdit_username.setSizePolicy(sizePolicy)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(5000, 5000))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setPlaceholderText("")
        self.lineEdit_username.setClearButtonEnabled(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 5, 1, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_SQLite_file = QtWidgets.QLineEdit(Form)
        self.lineEdit_SQLite_file.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_SQLite_file.sizePolicy().hasHeightForWidth())
        self.lineEdit_SQLite_file.setSizePolicy(sizePolicy)
        self.lineEdit_SQLite_file.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_SQLite_file.setFont(font)
        self.lineEdit_SQLite_file.setCursor(QtCore.Qt.IBeamCursor)
        self.lineEdit_SQLite_file.setPlaceholderText("")
        self.lineEdit_SQLite_file.setObjectName("lineEdit_SQLite_file")
        self.horizontalLayout_3.addWidget(self.lineEdit_SQLite_file)
        self.toolButton_browse = QtWidgets.QToolButton(Form)
        self.toolButton_browse.setEnabled(False)
        self.toolButton_browse.setMinimumSize(QtCore.QSize(0, 20))
        self.toolButton_browse.setMaximumSize(QtCore.QSize(23, 16777215))
        self.toolButton_browse.setObjectName("toolButton_browse")
        self.horizontalLayout_3.addWidget(self.toolButton_browse)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 2)
        self.lineEdit_database = QtWidgets.QLineEdit(Form)
        self.lineEdit_database.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_database.sizePolicy().hasHeightForWidth())
        self.lineEdit_database.setSizePolicy(sizePolicy)
        self.lineEdit_database.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_database.setMaximumSize(QtCore.QSize(5000, 5000))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_database.setFont(font)
        self.lineEdit_database.setPlaceholderText("")
        self.lineEdit_database.setClearButtonEnabled(True)
        self.lineEdit_database.setObjectName("lineEdit_database")
        self.gridLayout.addWidget(self.lineEdit_database, 4, 1, 1, 2)
        self.label_username = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 5, 0, 1, 1)
        self.label_host = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_host.sizePolicy().hasHeightForWidth())
        self.label_host.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_host.setFont(font)
        self.label_host.setObjectName("label_host")
        self.gridLayout.addWidget(self.label_host, 3, 0, 1, 1)
        self.label_database = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_database.sizePolicy().hasHeightForWidth())
        self.label_database.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_database.setFont(font)
        self.label_database.setObjectName("label_database")
        self.gridLayout.addWidget(self.label_database, 4, 0, 1, 1)
        self.label_dialect = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dialect.sizePolicy().hasHeightForWidth())
        self.label_dialect.setSizePolicy(sizePolicy)
        self.label_dialect.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_dialect.setFont(font)
        self.label_dialect.setObjectName("label_dialect")
        self.gridLayout.addWidget(self.label_dialect, 0, 0, 1, 1)
        self.label_password = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 6, 0, 1, 1)
        self.label_dsn = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dsn.sizePolicy().hasHeightForWidth())
        self.label_dsn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_dsn.setFont(font)
        self.label_dsn.setObjectName("label_dsn")
        self.gridLayout.addWidget(self.label_dsn, 1, 0, 1, 1)
        self.label_path = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_path.sizePolicy().hasHeightForWidth())
        self.label_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")
        self.gridLayout.addWidget(self.label_path, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_open_treeview = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open_treeview.sizePolicy().hasHeightForWidth())
        self.pushButton_open_treeview.setSizePolicy(sizePolicy)
        self.pushButton_open_treeview.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_open_treeview.setMaximumSize(QtCore.QSize(120, 23))
        self.pushButton_open_treeview.setObjectName("pushButton_open_treeview")
        self.horizontalLayout.addWidget(self.pushButton_open_treeview)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_open_directory = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open_directory.sizePolicy().hasHeightForWidth())
        self.pushButton_open_directory.setSizePolicy(sizePolicy)
        self.pushButton_open_directory.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_open_directory.setMaximumSize(QtCore.QSize(120, 23))
        self.pushButton_open_directory.setObjectName("pushButton_open_directory")
        self.horizontalLayout.addWidget(self.pushButton_open_directory)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox_dialect, self.toolButton_spine)
        Form.setTabOrder(self.toolButton_spine, self.comboBox_dsn)
        Form.setTabOrder(self.comboBox_dsn, self.lineEdit_SQLite_file)
        Form.setTabOrder(self.lineEdit_SQLite_file, self.toolButton_browse)
        Form.setTabOrder(self.toolButton_browse, self.lineEdit_host)
        Form.setTabOrder(self.lineEdit_host, self.lineEdit_port)
        Form.setTabOrder(self.lineEdit_port, self.lineEdit_database)
        Form.setTabOrder(self.lineEdit_database, self.lineEdit_username)
        Form.setTabOrder(self.lineEdit_username, self.lineEdit_password)
        Form.setTabOrder(self.lineEdit_password, self.pushButton_open_treeview)
        Form.setTabOrder(self.pushButton_open_treeview, self.pushButton_open_directory)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Data Store", None, -1))
        self.label_name.setText(QtWidgets.QApplication.translate("Form", "Name", None, -1))
        self.toolButton_spine.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Create fresh (empty) Spine database into an SQLite file in Data store\'s directory.</p></body></html>", None, -1))
        self.toolButton_spine.setText(QtWidgets.QApplication.translate("Form", "...", None, -1))
        self.lineEdit_password.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Password (optional)</p></body></html>", None, -1))
        self.lineEdit_host.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Host (required)</p></body></html>", None, -1))
        self.label_port.setText(QtWidgets.QApplication.translate("Form", "Port", None, -1))
        self.lineEdit_port.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Port (optional)</p></body></html>", None, -1))
        self.lineEdit_username.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Username (optional)</p></body></html>", None, -1))
        self.toolButton_browse.setText(QtWidgets.QApplication.translate("Form", "...", None, -1))
        self.lineEdit_database.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Database (required)</p></body></html>", None, -1))
        self.label_username.setText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.label_host.setText(QtWidgets.QApplication.translate("Form", "Host", None, -1))
        self.label_database.setText(QtWidgets.QApplication.translate("Form", "Database", None, -1))
        self.label_dialect.setText(QtWidgets.QApplication.translate("Form", "Dialect", None, -1))
        self.label_password.setText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.label_dsn.setText(QtWidgets.QApplication.translate("Form", "DSN", None, -1))
        self.label_path.setText(QtWidgets.QApplication.translate("Form", "Path", None, -1))
        self.pushButton_open_treeview.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Open Data Store directory in file browser</p></body></html>", None, -1))
        self.pushButton_open_treeview.setText(QtWidgets.QApplication.translate("Form", "Open treeview", None, -1))
        self.pushButton_open_directory.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>Open Data Store directory in file browser</p></body></html>", None, -1))
        self.pushButton_open_directory.setText(QtWidgets.QApplication.translate("Form", "Open directory...", None, -1))

import resources_icons_rc
