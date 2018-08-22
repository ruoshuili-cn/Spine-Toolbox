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

# Form implementation generated from reading ui file '../spinetoolbox/ui/data_store_form.ui',
# licensing of '../spinetoolbox/ui/data_store_form.ui' applies.
#
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.splitter_tree_parameter = QtWidgets.QSplitter(self.centralwidget)
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
        self.treeView_object = ObjectTreeView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_object.sizePolicy().hasHeightForWidth())
        self.treeView_object.setSizePolicy(sizePolicy)
        self.treeView_object.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView_object.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeView_object.setObjectName("treeView_object")
        self.verticalLayout_3.addWidget(self.treeView_object)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_tree_parameter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.tabWidget_object = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_object.sizePolicy().hasHeightForWidth())
        self.tabWidget_object.setSizePolicy(sizePolicy)
        self.tabWidget_object.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget_object.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_object.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_object.setObjectName("tabWidget_object")
        self.tab_object_parameter_value = QtWidgets.QWidget()
        self.tab_object_parameter_value.setObjectName("tab_object_parameter_value")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_object_parameter_value)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_object_parameter_value = QtWidgets.QLabel(self.tab_object_parameter_value)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_object_parameter_value.sizePolicy().hasHeightForWidth())
        self.label_object_parameter_value.setSizePolicy(sizePolicy)
        self.label_object_parameter_value.setObjectName("label_object_parameter_value")
        self.horizontalLayout.addWidget(self.label_object_parameter_value)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableView_object_parameter_value = CustomQTableView(self.tab_object_parameter_value)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_object_parameter_value.sizePolicy().hasHeightForWidth())
        self.tableView_object_parameter_value.setSizePolicy(sizePolicy)
        self.tableView_object_parameter_value.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_object_parameter_value.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_object_parameter_value.setSortingEnabled(True)
        self.tableView_object_parameter_value.setWordWrap(False)
        self.tableView_object_parameter_value.setObjectName("tableView_object_parameter_value")
        self.tableView_object_parameter_value.horizontalHeader().setHighlightSections(False)
        self.tableView_object_parameter_value.verticalHeader().setVisible(False)
        self.tableView_object_parameter_value.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.tableView_object_parameter_value)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget_object.addTab(self.tab_object_parameter_value, "")
        self.tab_object_parameter = QtWidgets.QWidget()
        self.tab_object_parameter.setObjectName("tab_object_parameter")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_object_parameter)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_object_parameter = QtWidgets.QLabel(self.tab_object_parameter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_object_parameter.sizePolicy().hasHeightForWidth())
        self.label_object_parameter.setSizePolicy(sizePolicy)
        self.label_object_parameter.setObjectName("label_object_parameter")
        self.horizontalLayout_4.addWidget(self.label_object_parameter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tableView_object_parameter = CustomQTableView(self.tab_object_parameter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_object_parameter.sizePolicy().hasHeightForWidth())
        self.tableView_object_parameter.setSizePolicy(sizePolicy)
        self.tableView_object_parameter.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_object_parameter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_object_parameter.setSortingEnabled(True)
        self.tableView_object_parameter.setWordWrap(False)
        self.tableView_object_parameter.setObjectName("tableView_object_parameter")
        self.tableView_object_parameter.horizontalHeader().setHighlightSections(False)
        self.tableView_object_parameter.verticalHeader().setVisible(False)
        self.tableView_object_parameter.verticalHeader().setHighlightSections(False)
        self.verticalLayout_5.addWidget(self.tableView_object_parameter)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget_object.addTab(self.tab_object_parameter, "")
        self.tabWidget_relationship = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_relationship.sizePolicy().hasHeightForWidth())
        self.tabWidget_relationship.setSizePolicy(sizePolicy)
        self.tabWidget_relationship.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget_relationship.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_relationship.setObjectName("tabWidget_relationship")
        self.tab_relationship_parameter_value = QtWidgets.QWidget()
        self.tab_relationship_parameter_value.setObjectName("tab_relationship_parameter_value")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_relationship_parameter_value)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_relationship_parameter_value = QtWidgets.QLabel(self.tab_relationship_parameter_value)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_relationship_parameter_value.sizePolicy().hasHeightForWidth())
        self.label_relationship_parameter_value.setSizePolicy(sizePolicy)
        self.label_relationship_parameter_value.setObjectName("label_relationship_parameter_value")
        self.horizontalLayout_3.addWidget(self.label_relationship_parameter_value)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableView_relationship_parameter_value = CustomQTableView(self.tab_relationship_parameter_value)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_relationship_parameter_value.sizePolicy().hasHeightForWidth())
        self.tableView_relationship_parameter_value.setSizePolicy(sizePolicy)
        self.tableView_relationship_parameter_value.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_relationship_parameter_value.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_relationship_parameter_value.setSortingEnabled(True)
        self.tableView_relationship_parameter_value.setWordWrap(False)
        self.tableView_relationship_parameter_value.setObjectName("tableView_relationship_parameter_value")
        self.tableView_relationship_parameter_value.horizontalHeader().setHighlightSections(False)
        self.tableView_relationship_parameter_value.verticalHeader().setVisible(False)
        self.tableView_relationship_parameter_value.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tableView_relationship_parameter_value)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.tabWidget_relationship.addTab(self.tab_relationship_parameter_value, "")
        self.tab_relationship_parameter = QtWidgets.QWidget()
        self.tab_relationship_parameter.setObjectName("tab_relationship_parameter")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_relationship_parameter)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_relationship_parameter = QtWidgets.QLabel(self.tab_relationship_parameter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_relationship_parameter.sizePolicy().hasHeightForWidth())
        self.label_relationship_parameter.setSizePolicy(sizePolicy)
        self.label_relationship_parameter.setObjectName("label_relationship_parameter")
        self.horizontalLayout_5.addWidget(self.label_relationship_parameter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.tableView_relationship_parameter = CustomQTableView(self.tab_relationship_parameter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_relationship_parameter.sizePolicy().hasHeightForWidth())
        self.tableView_relationship_parameter.setSizePolicy(sizePolicy)
        self.tableView_relationship_parameter.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_relationship_parameter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_relationship_parameter.setSortingEnabled(True)
        self.tableView_relationship_parameter.setWordWrap(False)
        self.tableView_relationship_parameter.setObjectName("tableView_relationship_parameter")
        self.tableView_relationship_parameter.horizontalHeader().setHighlightSections(False)
        self.tableView_relationship_parameter.verticalHeader().setVisible(False)
        self.tableView_relationship_parameter.verticalHeader().setHighlightSections(False)
        self.verticalLayout_7.addWidget(self.tableView_relationship_parameter)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.tabWidget_relationship.addTab(self.tab_relationship_parameter, "")
        self.horizontalLayout_6.addWidget(self.splitter)
        self.verticalLayout_10.addWidget(self.splitter_tree_parameter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuSession = QtWidgets.QMenu(self.menubar)
        self.menuSession.setObjectName("menuSession")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCommit = QtWidgets.QAction(MainWindow)
        self.actionCommit.setObjectName("actionCommit")
        self.actionRollback = QtWidgets.QAction(MainWindow)
        self.actionRollback.setObjectName("actionRollback")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_object_classes = QtWidgets.QAction(MainWindow)
        self.actionAdd_object_classes.setObjectName("actionAdd_object_classes")
        self.actionAdd_objects = QtWidgets.QAction(MainWindow)
        self.actionAdd_objects.setObjectName("actionAdd_objects")
        self.actionAdd_relationship_classes = QtWidgets.QAction(MainWindow)
        self.actionAdd_relationship_classes.setObjectName("actionAdd_relationship_classes")
        self.actionAdd_relationships = QtWidgets.QAction(MainWindow)
        self.actionAdd_relationships.setObjectName("actionAdd_relationships")
        self.actionAdd_parameters = QtWidgets.QAction(MainWindow)
        self.actionAdd_parameters.setObjectName("actionAdd_parameters")
        self.actionAdd_parameter_values = QtWidgets.QAction(MainWindow)
        self.actionAdd_parameter_values.setObjectName("actionAdd_parameter_values")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuSession.addSeparator()
        self.menuSession.addAction(self.actionCommit)
        self.menuSession.addAction(self.actionRollback)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd_object_classes)
        self.menuEdit.addAction(self.actionAdd_objects)
        self.menuEdit.addAction(self.actionAdd_relationship_classes)
        self.menuEdit.addAction(self.actionAdd_relationships)
        self.menuEdit.addAction(self.actionAdd_parameters)
        self.menuEdit.addAction(self.actionAdd_parameter_values)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSession.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_object.setCurrentIndex(0)
        self.tabWidget_relationship.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_object_tree.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Object tree</b>", None, -1))
        self.label_object_parameter_value.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Object parameter</b>", None, -1))
        self.tabWidget_object.setTabText(self.tabWidget_object.indexOf(self.tab_object_parameter_value), QtWidgets.QApplication.translate("MainWindow", "Value", None, -1))
        self.label_object_parameter.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Object parameter</b>", None, -1))
        self.tabWidget_object.setTabText(self.tabWidget_object.indexOf(self.tab_object_parameter), QtWidgets.QApplication.translate("MainWindow", "Definition", None, -1))
        self.label_relationship_parameter_value.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Relationship parameter</b>", None, -1))
        self.tabWidget_relationship.setTabText(self.tabWidget_relationship.indexOf(self.tab_relationship_parameter_value), QtWidgets.QApplication.translate("MainWindow", "Value", None, -1))
        self.label_relationship_parameter.setText(QtWidgets.QApplication.translate("MainWindow", "<b>Relationship parameter</b>", None, -1))
        self.tabWidget_relationship.setTabText(self.tabWidget_relationship.indexOf(self.tab_relationship_parameter), QtWidgets.QApplication.translate("MainWindow", "Definition", None, -1))
        self.menuSession.setTitle(QtWidgets.QApplication.translate("MainWindow", "Session", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionCommit.setText(QtWidgets.QApplication.translate("MainWindow", "Commit", None, -1))
        self.actionCommit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Return", None, -1))
        self.actionRollback.setText(QtWidgets.QApplication.translate("MainWindow", "Rollback", None, -1))
        self.actionRollback.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Backspace", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.actionQuit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionAdd_object_classes.setText(QtWidgets.QApplication.translate("MainWindow", "Add object classes", None, -1))
        self.actionAdd_object_classes.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add object classes", None, -1))
        self.actionAdd_object_classes.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+O", None, -1))
        self.actionAdd_objects.setText(QtWidgets.QApplication.translate("MainWindow", "Add objects", None, -1))
        self.actionAdd_objects.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add objects", None, -1))
        self.actionAdd_objects.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionAdd_relationship_classes.setText(QtWidgets.QApplication.translate("MainWindow", "Add relationship classes", None, -1))
        self.actionAdd_relationship_classes.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add relationship classes", None, -1))
        self.actionAdd_relationship_classes.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+R", None, -1))
        self.actionAdd_relationships.setText(QtWidgets.QApplication.translate("MainWindow", "Add relationships", None, -1))
        self.actionAdd_relationships.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add relationships", None, -1))
        self.actionAdd_relationships.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+R", None, -1))
        self.actionAdd_parameters.setText(QtWidgets.QApplication.translate("MainWindow", "Add parameters", None, -1))
        self.actionAdd_parameters.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add parameters", None, -1))
        self.actionAdd_parameters.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+P", None, -1))
        self.actionAdd_parameter_values.setText(QtWidgets.QApplication.translate("MainWindow", "Add parameter values", None, -1))
        self.actionAdd_parameter_values.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add parameter values", None, -1))
        self.actionAdd_parameter_values.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+P", None, -1))
        self.actionImport.setText(QtWidgets.QApplication.translate("MainWindow", "Import", None, -1))
        self.actionImport.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+I", None, -1))
        self.actionExport.setText(QtWidgets.QApplication.translate("MainWindow", "Export", None, -1))
        self.actionExport.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+E", None, -1))
        self.actionConnect.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.actionCopy.setText(QtWidgets.QApplication.translate("MainWindow", "Copy", None, -1))
        self.actionCopy.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+C", None, -1))
        self.actionPaste.setText(QtWidgets.QApplication.translate("MainWindow", "Paste", None, -1))
        self.actionPaste.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+V", None, -1))

from widgets.custom_qtableview import CustomQTableView
from widgets.custom_qtreeview import ObjectTreeView
