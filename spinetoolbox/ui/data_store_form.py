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

# Form implementation generated from reading ui file '../spinetoolbox/ui/data_store_form.ui'
#
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(781, 494)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.splitter_tree_parameter = QtWidgets.QSplitter(Form)
        self.splitter_tree_parameter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_tree_parameter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_tree_parameter.setHandleWidth(6)
        self.splitter_tree_parameter.setObjectName("splitter_tree_parameter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_tree_parameter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_object_tree = QtWidgets.QLabel(self.layoutWidget)
        self.label_object_tree.setObjectName("label_object_tree")
        self.verticalLayout_3.addWidget(self.label_object_tree)
        self.treeView_object = CustomQTreeView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_object.sizePolicy().hasHeightForWidth())
        self.treeView_object.setSizePolicy(sizePolicy)
        self.treeView_object.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView_object.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeView_object.setObjectName("treeView_object")
        self.verticalLayout_3.addWidget(self.treeView_object)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_tree_parameter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_object_parameter = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_object_parameter.sizePolicy().hasHeightForWidth())
        self.label_object_parameter.setSizePolicy(sizePolicy)
        self.label_object_parameter.setObjectName("label_object_parameter")
        self.horizontalLayout.addWidget(self.label_object_parameter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableView_object_parameter_value = CustomQTableView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_object_parameter_value.sizePolicy().hasHeightForWidth())
        self.tableView_object_parameter_value.setSizePolicy(sizePolicy)
        self.tableView_object_parameter_value.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_object_parameter_value.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_object_parameter_value.setSortingEnabled(True)
        self.tableView_object_parameter_value.setObjectName("tableView_object_parameter_value")
        self.verticalLayout_2.addWidget(self.tableView_object_parameter_value)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_object_parameter_def = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_object_parameter_def.sizePolicy().hasHeightForWidth())
        self.label_object_parameter_def.setSizePolicy(sizePolicy)
        self.label_object_parameter_def.setObjectName("label_object_parameter_def")
        self.horizontalLayout_4.addWidget(self.label_object_parameter_def)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tableView_object_parameter = CustomQTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_object_parameter.sizePolicy().hasHeightForWidth())
        self.tableView_object_parameter.setSizePolicy(sizePolicy)
        self.tableView_object_parameter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_object_parameter.setSortingEnabled(True)
        self.tableView_object_parameter.setObjectName("tableView_object_parameter")
        self.verticalLayout_5.addWidget(self.tableView_object_parameter)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_relationship_parameter = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_relationship_parameter.sizePolicy().hasHeightForWidth())
        self.label_relationship_parameter.setSizePolicy(sizePolicy)
        self.label_relationship_parameter.setObjectName("label_relationship_parameter")
        self.horizontalLayout_3.addWidget(self.label_relationship_parameter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView_relationship_parameter_value = CustomQTableView(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_relationship_parameter_value.sizePolicy().hasHeightForWidth())
        self.tableView_relationship_parameter_value.setSizePolicy(sizePolicy)
        self.tableView_relationship_parameter_value.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_relationship_parameter_value.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_relationship_parameter_value.setSortingEnabled(True)
        self.tableView_relationship_parameter_value.setObjectName("tableView_relationship_parameter_value")
        self.verticalLayout.addWidget(self.tableView_relationship_parameter_value)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_relationship_parameter_def = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_relationship_parameter_def.sizePolicy().hasHeightForWidth())
        self.label_relationship_parameter_def.setSizePolicy(sizePolicy)
        self.label_relationship_parameter_def.setObjectName("label_relationship_parameter_def")
        self.horizontalLayout_5.addWidget(self.label_relationship_parameter_def)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.tableView_relationship_parameter = CustomQTableView(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_relationship_parameter.sizePolicy().hasHeightForWidth())
        self.tableView_relationship_parameter.setSizePolicy(sizePolicy)
        self.tableView_relationship_parameter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_relationship_parameter.setSortingEnabled(True)
        self.tableView_relationship_parameter.setObjectName("tableView_relationship_parameter")
        self.verticalLayout_7.addWidget(self.tableView_relationship_parameter)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.horizontalLayout_6.addWidget(self.splitter)
        self.verticalLayout_10.addWidget(self.splitter_tree_parameter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_commit_msg = QtWidgets.QLineEdit(Form)
        self.lineEdit_commit_msg.setObjectName("lineEdit_commit_msg")
        self.horizontalLayout_2.addWidget(self.lineEdit_commit_msg)
        self.pushButton_commit = QtWidgets.QPushButton(Form)
        self.pushButton_commit.setObjectName("pushButton_commit")
        self.horizontalLayout_2.addWidget(self.pushButton_commit)
        self.pushButton_revert = QtWidgets.QPushButton(Form)
        self.pushButton_revert.setObjectName("pushButton_revert")
        self.horizontalLayout_2.addWidget(self.pushButton_revert)
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
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
        self.verticalLayout_11.addLayout(self.horizontalLayout_statusbar_placeholder)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Spine Data Explorer", None, -1))
        self.label_object_tree.setText(QtWidgets.QApplication.translate("Form", "<b>Object tree</b>", None, -1))
        self.label_object_parameter.setText(QtWidgets.QApplication.translate("Form", "<b>Object parameter</b>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("Form", "Value", None, -1))
        self.label_object_parameter_def.setText(QtWidgets.QApplication.translate("Form", "<b>Object parameter</b>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("Form", "Definition", None, -1))
        self.label_relationship_parameter.setText(QtWidgets.QApplication.translate("Form", "<b>Relationship parameter</b>", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtWidgets.QApplication.translate("Form", "Value", None, -1))
        self.label_relationship_parameter_def.setText(QtWidgets.QApplication.translate("Form", "<b>Relationship parameter</b>", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtWidgets.QApplication.translate("Form", "Definition", None, -1))
        self.lineEdit_commit_msg.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Enter commit message here...", None, -1))
        self.pushButton_commit.setText(QtWidgets.QApplication.translate("Form", "Commit", None, -1))
        self.pushButton_revert.setText(QtWidgets.QApplication.translate("Form", "Revert", None, -1))
        self.pushButton_close.setText(QtWidgets.QApplication.translate("Form", "Close", None, -1))

from widgets.custom_qtableview import CustomQTableView
from widgets.custom_qtreeview import CustomQTreeView
import resources_icons_rc
