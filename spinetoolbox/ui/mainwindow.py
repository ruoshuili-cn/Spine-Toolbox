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

# Form implementation generated from reading ui file '../spinetoolbox/ui/mainwindow.ui',
# licensing of '../spinetoolbox/ui/mainwindow.ui' applies.
#
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 23))
        self.label.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.graphicsView = CustomQGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.Panel)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsView.setMidLineWidth(0)
        self.graphicsView.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_10.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuToolbars = QtWidgets.QMenu(self.menuView)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menuDock_Widgets = QtWidgets.QMenu(self.menuView)
        self.menuDock_Widgets.setObjectName("menuDock_Widgets")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_eventlog = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_eventlog.sizePolicy().hasHeightForWidth())
        self.dockWidget_eventlog.setSizePolicy(sizePolicy)
        self.dockWidget_eventlog.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_eventlog.setObjectName("dockWidget_eventlog")
        self.dockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_eventlog = CustomQTextBrowser(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_eventlog.sizePolicy().hasHeightForWidth())
        self.textBrowser_eventlog.setSizePolicy(sizePolicy)
        self.textBrowser_eventlog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser_eventlog.setOpenLinks(False)
        self.textBrowser_eventlog.setObjectName("textBrowser_eventlog")
        self.verticalLayout_3.addWidget(self.textBrowser_eventlog)
        self.dockWidget_eventlog.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_eventlog)
        self.dockWidget_process_output = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_process_output.sizePolicy().hasHeightForWidth())
        self.dockWidget_process_output.setSizePolicy(sizePolicy)
        self.dockWidget_process_output.setMinimumSize(QtCore.QSize(91, 133))
        self.dockWidget_process_output.setObjectName("dockWidget_process_output")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textBrowser_process_output = CustomQTextBrowser(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_process_output.sizePolicy().hasHeightForWidth())
        self.textBrowser_process_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.textBrowser_process_output.setFont(font)
        self.textBrowser_process_output.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser_process_output.setOpenLinks(False)
        self.textBrowser_process_output.setObjectName("textBrowser_process_output")
        self.verticalLayout_6.addWidget(self.textBrowser_process_output)
        self.dockWidget_process_output.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_process_output)
        self.dockWidget_item = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_item.setMinimumSize(QtCore.QSize(140, 138))
        self.dockWidget_item.setObjectName("dockWidget_item")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_subwindow = QtWidgets.QGroupBox(self.dockWidgetContents_3)
        self.groupBox_subwindow.setObjectName("groupBox_subwindow")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_subwindow)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget = QtWidgets.QWidget(self.groupBox_subwindow)
        self.widget.setObjectName("widget")
        self.verticalLayout_8.addWidget(self.widget)
        self.verticalLayout.addWidget(self.groupBox_subwindow)
        self.dockWidget_item.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_item)
        self.dockWidget_julia_repl = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_julia_repl.setObjectName("dockWidget_julia_repl")
        self.dockWidgetContents_julia_repl = QtWidgets.QWidget()
        self.dockWidgetContents_julia_repl.setObjectName("dockWidgetContents_julia_repl")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.dockWidgetContents_julia_repl)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_2 = QtWidgets.QWidget(self.dockWidgetContents_julia_repl)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_9.addWidget(self.widget_2)
        self.dockWidget_julia_repl.setWidget(self.dockWidgetContents_julia_repl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_julia_repl)
        self.dockWidget_project = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_project.setObjectName("dockWidget_project")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_items = QtWidgets.QWidget()
        self.tab_items.setObjectName("tab_items")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeView_project = QtWidgets.QTreeView(self.tab_items)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_project.sizePolicy().hasHeightForWidth())
        self.treeView_project.setSizePolicy(sizePolicy)
        self.treeView_project.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView_project.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView_project.setObjectName("treeView_project")
        self.verticalLayout_2.addWidget(self.treeView_project)
        self.tabWidget.addTab(self.tab_items, "")
        self.tab_tool_templates = QtWidgets.QWidget()
        self.tab_tool_templates.setObjectName("tab_tool_templates")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_tool_templates)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.listView_tool_templates = QtWidgets.QListView(self.tab_tool_templates)
        self.listView_tool_templates.setObjectName("listView_tool_templates")
        self.verticalLayout_5.addWidget(self.listView_tool_templates)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add_tool_template = QtWidgets.QPushButton(self.tab_tool_templates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_tool_template.sizePolicy().hasHeightForWidth())
        self.pushButton_add_tool_template.setSizePolicy(sizePolicy)
        self.pushButton_add_tool_template.setMinimumSize(QtCore.QSize(26, 26))
        self.pushButton_add_tool_template.setMaximumSize(QtCore.QSize(26, 26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/add_tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add_tool_template.setIcon(icon)
        self.pushButton_add_tool_template.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_add_tool_template.setObjectName("pushButton_add_tool_template")
        self.horizontalLayout.addWidget(self.pushButton_add_tool_template)
        self.pushButton_refresh_tool_templates = QtWidgets.QPushButton(self.tab_tool_templates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh_tool_templates.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh_tool_templates.setSizePolicy(sizePolicy)
        self.pushButton_refresh_tool_templates.setMinimumSize(QtCore.QSize(26, 26))
        self.pushButton_refresh_tool_templates.setMaximumSize(QtCore.QSize(26, 26))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/refresh_tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refresh_tool_templates.setIcon(icon1)
        self.pushButton_refresh_tool_templates.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_refresh_tool_templates.setObjectName("pushButton_refresh_tool_templates")
        self.horizontalLayout.addWidget(self.pushButton_refresh_tool_templates)
        self.pushButton_remove_tool_template = QtWidgets.QPushButton(self.tab_tool_templates)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove_tool_template.sizePolicy().hasHeightForWidth())
        self.pushButton_remove_tool_template.setSizePolicy(sizePolicy)
        self.pushButton_remove_tool_template.setMinimumSize(QtCore.QSize(26, 26))
        self.pushButton_remove_tool_template.setMaximumSize(QtCore.QSize(26, 26))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/remove_tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_remove_tool_template.setIcon(icon2)
        self.pushButton_remove_tool_template.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_remove_tool_template.setObjectName("pushButton_remove_tool_template")
        self.horizontalLayout.addWidget(self.pushButton_remove_tool_template)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_tool_templates, "")
        self.tab_connections = QtWidgets.QWidget()
        self.tab_connections.setObjectName("tab_connections")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_connections)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableView_connections = QtWidgets.QTableView(self.tab_connections)
        self.tableView_connections.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableView_connections.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableView_connections.setCornerButtonEnabled(False)
        self.tableView_connections.setObjectName("tableView_connections")
        self.tableView_connections.horizontalHeader().setHighlightSections(False)
        self.tableView_connections.horizontalHeader().setMinimumSectionSize(35)
        self.tableView_connections.horizontalHeader().setStretchLastSection(False)
        self.tableView_connections.verticalHeader().setHighlightSections(False)
        self.verticalLayout_7.addWidget(self.tableView_connections)
        self.tabWidget.addTab(self.tab_connections, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.dockWidget_project.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_project)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionData_Store = QtWidgets.QAction(MainWindow)
        self.actionData_Store.setObjectName("actionData_Store")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_Data_Connection = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/dc_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Data_Connection.setIcon(icon3)
        self.actionAdd_Data_Connection.setObjectName("actionAdd_Data_Connection")
        self.actionAdd_Data_Store = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/ds_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Data_Store.setIcon(icon4)
        self.actionAdd_Data_Store.setObjectName("actionAdd_Data_Store")
        self.actionAdd_Tool = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/tool_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Tool.setIcon(icon5)
        self.actionAdd_Tool.setObjectName("actionAdd_Tool")
        self.actionAdd_View = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/view_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_View.setIcon(icon6)
        self.actionAdd_View.setObjectName("actionAdd_View")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionItem_Toolbar = QtWidgets.QAction(MainWindow)
        self.actionItem_Toolbar.setObjectName("actionItem_Toolbar")
        self.actionAdd_Item_Toolbar = QtWidgets.QAction(MainWindow)
        self.actionAdd_Item_Toolbar.setObjectName("actionAdd_Item_Toolbar")
        self.actionEvent_Log = QtWidgets.QAction(MainWindow)
        self.actionEvent_Log.setCheckable(False)
        self.actionEvent_Log.setChecked(False)
        self.actionEvent_Log.setObjectName("actionEvent_Log")
        self.actionSubprocess_Output = QtWidgets.QAction(MainWindow)
        self.actionSubprocess_Output.setObjectName("actionSubprocess_Output")
        self.actionSelected_Item = QtWidgets.QAction(MainWindow)
        self.actionSelected_Item.setObjectName("actionSelected_Item")
        self.actionJulia_REPL = QtWidgets.QAction(MainWindow)
        self.actionJulia_REPL.setObjectName("actionJulia_REPL")
        self.actionUser_Guide = QtWidgets.QAction(MainWindow)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionAdd_Data_Store)
        self.menuEdit.addAction(self.actionAdd_Data_Connection)
        self.menuEdit.addAction(self.actionAdd_Tool)
        self.menuEdit.addAction(self.actionAdd_View)
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuView.addAction(self.menuDock_Widgets.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.treeView_project)
        MainWindow.setTabOrder(self.treeView_project, self.listView_tool_templates)
        MainWindow.setTabOrder(self.listView_tool_templates, self.pushButton_add_tool_template)
        MainWindow.setTabOrder(self.pushButton_add_tool_template, self.pushButton_refresh_tool_templates)
        MainWindow.setTabOrder(self.pushButton_refresh_tool_templates, self.pushButton_remove_tool_template)
        MainWindow.setTabOrder(self.pushButton_remove_tool_template, self.textBrowser_eventlog)
        MainWindow.setTabOrder(self.textBrowser_eventlog, self.textBrowser_process_output)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Spine Toolbox", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Main View", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.menuView.setTitle(QtWidgets.QApplication.translate("MainWindow", "View", None, -1))
        self.menuToolbars.setTitle(QtWidgets.QApplication.translate("MainWindow", "Toolbars", None, -1))
        self.menuDock_Widgets.setTitle(QtWidgets.QApplication.translate("MainWindow", "Dock Widgets", None, -1))
        self.dockWidget_eventlog.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Event Log", None, -1))
        self.dockWidget_process_output.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Subprocess Output", None, -1))
        self.dockWidget_item.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Item Info", None, -1))
        self.dockWidget_julia_repl.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Julia REPL", None, -1))
        self.dockWidget_project.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Project", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_items), QtWidgets.QApplication.translate("MainWindow", "Items", None, -1))
        self.listView_tool_templates.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Tool Templates available in this project</p></body></html>", None, -1))
        self.pushButton_add_tool_template.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Create new or add an existing Tool template to project</p></body></html>", None, -1))
        self.pushButton_refresh_tool_templates.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Refresh Tool templates</p></body></html>", None, -1))
        self.pushButton_remove_tool_template.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Remove (selected) Tool template from project</p></body></html>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tool_templates), QtWidgets.QApplication.translate("MainWindow", "Templates", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_connections), QtWidgets.QApplication.translate("MainWindow", "Connections", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.actionQuit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionData_Store.setText(QtWidgets.QApplication.translate("MainWindow", "Data Store", None, -1))
        self.actionDocumentation.setText(QtWidgets.QApplication.translate("MainWindow", "Documentation", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionAbout.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F12", None, -1))
        self.actionAdd_Data_Connection.setText(QtWidgets.QApplication.translate("MainWindow", "Add Data Connection", None, -1))
        self.actionAdd_Data_Store.setText(QtWidgets.QApplication.translate("MainWindow", "Add Data Store", None, -1))
        self.actionAdd_Tool.setText(QtWidgets.QApplication.translate("MainWindow", "Add Tool", None, -1))
        self.actionAdd_View.setText(QtWidgets.QApplication.translate("MainWindow", "Add View", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionSave_As.setText(QtWidgets.QApplication.translate("MainWindow", "Save As...", None, -1))
        self.actionSave_As.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Duplicate project under a new name", None, -1))
        self.actionSave_As.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open...", None, -1))
        self.actionOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionNew.setText(QtWidgets.QApplication.translate("MainWindow", "New...", None, -1))
        self.actionNew.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None, -1))
        self.actionSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings...", None, -1))
        self.actionSettings.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F1", None, -1))
        self.actionItem_Toolbar.setText(QtWidgets.QApplication.translate("MainWindow", "Item Toolbar", None, -1))
        self.actionAdd_Item_Toolbar.setText(QtWidgets.QApplication.translate("MainWindow", "Add Item Toolbar", None, -1))
        self.actionAdd_Item_Toolbar.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Make Add Item Toolbar visible</p></body></html>", None, -1))
        self.actionEvent_Log.setText(QtWidgets.QApplication.translate("MainWindow", "Event Log", None, -1))
        self.actionEvent_Log.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Make Event Log widget visible</p></body></html>", None, -1))
        self.actionSubprocess_Output.setText(QtWidgets.QApplication.translate("MainWindow", "Subprocess Output", None, -1))
        self.actionSubprocess_Output.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Make Subprocess Output widget visible</p></body></html>", None, -1))
        self.actionSelected_Item.setText(QtWidgets.QApplication.translate("MainWindow", "Selected Item", None, -1))
        self.actionSelected_Item.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Make Selected Item widget visible</p></body></html>", None, -1))
        self.actionJulia_REPL.setText(QtWidgets.QApplication.translate("MainWindow", "Julia REPL", None, -1))
        self.actionJulia_REPL.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Make Julia REPL widget visible</p></body></html>", None, -1))
        self.actionUser_Guide.setText(QtWidgets.QApplication.translate("MainWindow", "User Guide", None, -1))
        self.actionUser_Guide.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F2", None, -1))

from widgets.custom_qtextbrowser import CustomQTextBrowser
from widgets.custom_qgraphicsview import CustomQGraphicsView
import resources_icons_rc
