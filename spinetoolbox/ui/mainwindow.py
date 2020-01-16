# -*- coding: utf-8 -*-
######################################################################################################################
# Copyright (C) 2017-2020 Spine project consortium
# This file is part of Spine Toolbox.
# Spine Toolbox is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option)
# any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General
# Public License for more details. You should have received a copy of the GNU Lesser General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
######################################################################################################################

# Form implementation generated from reading ui file 'C:\data\src\toolbox\bin\..\spinetoolbox\ui\mainwindow.ui',
# licensing of 'C:\data\src\toolbox\bin\..\spinetoolbox\ui\mainwindow.ui' applies.
#
# Created: Thu Jan 16 08:36:11 2020
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 708)
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
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMargin(0)
        self.label.setIndent(5)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.graphicsView = DesignQGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsView.setMidLineWidth(0)
        self.graphicsView.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_10.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 28))
        self.menubar.setNativeMenuBar(False)
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
        self.dockWidget_eventlog.setMinimumSize(QtCore.QSize(95, 113))
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
        self.dockWidget_process_output.setMinimumSize(QtCore.QSize(95, 113))
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
        self.dockWidget_item.setMinimumSize(QtCore.QSize(356, 293))
        self.dockWidget_item.setObjectName("dockWidget_item")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_item_properties = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        self.tabWidget_item_properties.setStyleSheet("")
        self.tabWidget_item_properties.setObjectName("tabWidget_item_properties")
        self.tab_no_selection = QtWidgets.QWidget()
        self.tab_no_selection.setObjectName("tab_no_selection")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_no_selection)
        self.verticalLayout_14.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_no_selection = QtWidgets.QLabel(self.tab_no_selection)
        self.label_no_selection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_no_selection.setObjectName("label_no_selection")
        self.verticalLayout_14.addWidget(self.label_no_selection)
        self.tabWidget_item_properties.addTab(self.tab_no_selection, "")
        self.verticalLayout.addWidget(self.tabWidget_item_properties)
        self.dockWidget_item.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_item)
        self.dockWidget_julia_repl = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_julia_repl.setMinimumSize(QtCore.QSize(95, 80))
        self.dockWidget_julia_repl.setObjectName("dockWidget_julia_repl")
        self.dockWidgetContents_julia_repl = QtWidgets.QWidget()
        self.dockWidgetContents_julia_repl.setObjectName("dockWidgetContents_julia_repl")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.dockWidgetContents_julia_repl)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dockWidget_julia_repl.setWidget(self.dockWidgetContents_julia_repl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_julia_repl)
        self.dockWidget_project = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_project.setMinimumSize(QtCore.QSize(136, 320))
        self.dockWidget_project.setObjectName("dockWidget_project")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.dockWidgetContents_4)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.treeView_project = QtWidgets.QTreeView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_project.sizePolicy().hasHeightForWidth())
        self.treeView_project.setSizePolicy(sizePolicy)
        self.treeView_project.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView_project.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView_project.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView_project.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeView_project.setAnimated(True)
        self.treeView_project.setObjectName("treeView_project")
        self.verticalLayout_5.addWidget(self.treeView_project)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listView_tool_specifications = QtWidgets.QListView(self.layoutWidget1)
        self.listView_tool_specifications.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listView_tool_specifications.setObjectName("listView_tool_specifications")
        self.verticalLayout_2.addWidget(self.listView_tool_specifications)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_add_tool_specification = QtWidgets.QToolButton(self.dockWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_add_tool_specification.sizePolicy().hasHeightForWidth())
        self.toolButton_add_tool_specification.setSizePolicy(sizePolicy)
        self.toolButton_add_tool_specification.setMinimumSize(QtCore.QSize(26, 26))
        self.toolButton_add_tool_specification.setMaximumSize(QtCore.QSize(26, 26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wrench_plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_add_tool_specification.setIcon(icon)
        self.toolButton_add_tool_specification.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_add_tool_specification.setObjectName("toolButton_add_tool_specification")
        self.horizontalLayout.addWidget(self.toolButton_add_tool_specification)
        self.toolButton_remove_tool_specification = QtWidgets.QToolButton(self.dockWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_remove_tool_specification.sizePolicy().hasHeightForWidth())
        self.toolButton_remove_tool_specification.setSizePolicy(sizePolicy)
        self.toolButton_remove_tool_specification.setMinimumSize(QtCore.QSize(26, 26))
        self.toolButton_remove_tool_specification.setMaximumSize(QtCore.QSize(26, 26))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/wrench_minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_remove_tool_specification.setIcon(icon1)
        self.toolButton_remove_tool_specification.setObjectName("toolButton_remove_tool_specification")
        self.horizontalLayout.addWidget(self.toolButton_remove_tool_specification)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.dockWidget_project.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_project)
        self.dockWidget_python_repl = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_python_repl.setFloating(False)
        self.dockWidget_python_repl.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_python_repl.setObjectName("dockWidget_python_repl")
        self.dockWidgetContents_python_repl = QtWidgets.QWidget()
        self.dockWidgetContents_python_repl.setObjectName("dockWidgetContents_python_repl")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.dockWidgetContents_python_repl)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.dockWidget_python_repl.setWidget(self.dockWidgetContents_python_repl)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_python_repl)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/menu_icons/window-close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionData_Store = QtWidgets.QAction(MainWindow)
        self.actionData_Store.setObjectName("actionData_Store")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/menu_icons/info-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_Data_Connection = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/project_item_icons/file-alt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Data_Connection.setIcon(icon4)
        self.actionAdd_Data_Connection.setObjectName("actionAdd_Data_Connection")
        self.actionAdd_Data_Store = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/project_item_icons/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Data_Store.setIcon(icon5)
        self.actionAdd_Data_Store.setObjectName("actionAdd_Data_Store")
        self.actionAdd_Tool = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/project_item_icons/hammer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Tool.setIcon(icon6)
        self.actionAdd_Tool.setObjectName("actionAdd_Tool")
        self.actionAdd_View = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/project_item_icons/binoculars.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_View.setIcon(icon7)
        self.actionAdd_View.setObjectName("actionAdd_View")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/menu_icons/save_solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon8)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/menu_icons/save_regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon9)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/menu_icons/folder-open-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon10)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/menu_icons/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon11)
        self.actionNew.setObjectName("actionNew")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/menu_icons/cog.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon12)
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/menu_icons/question-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUser_Guide.setIcon(icon13)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.actionRestore_Dock_Widgets = QtWidgets.QAction(MainWindow)
        self.actionRestore_Dock_Widgets.setObjectName("actionRestore_Dock_Widgets")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/qt_extended_48x48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Qt.setIcon(icon14)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionPackages = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/menu_icons/hands-helping.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPackages.setIcon(icon15)
        self.actionPackages.setObjectName("actionPackages")
        self.actionRemove_all = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/menu_icons/trash-alt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_all.setIcon(icon16)
        self.actionRemove_all.setObjectName("actionRemove_all")
        self.actionExport_project_to_GraphML = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/menu_icons/file-export.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_project_to_GraphML.setIcon(icon17)
        self.actionExport_project_to_GraphML.setObjectName("actionExport_project_to_GraphML")
        self.actionAdd_Importer = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/project_item_icons/map-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Importer.setIcon(icon18)
        self.actionAdd_Importer.setObjectName("actionAdd_Importer")
        self.actionGetting_started = QtWidgets.QAction(MainWindow)
        self.actionGetting_started.setIcon(icon13)
        self.actionGetting_started.setObjectName("actionGetting_started")
        self.actionOpen_recent = QtWidgets.QAction(MainWindow)
        self.actionOpen_recent.setObjectName("actionOpen_recent")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDuplicate = QtWidgets.QAction(MainWindow)
        self.actionDuplicate.setObjectName("actionDuplicate")
        self.actionLive_tutorial = QtWidgets.QAction(MainWindow)
        self.actionLive_tutorial.setIcon(icon13)
        self.actionLive_tutorial.setObjectName("actionLive_tutorial")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_recent)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExport_project_to_GraphML)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionPackages)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addAction(self.actionGetting_started)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionRemove_all)
        self.menuDock_Widgets.addAction(self.actionRestore_Dock_Widgets)
        self.menuDock_Widgets.addSeparator()
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuView.addAction(self.menuDock_Widgets.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_item_properties.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.treeView_project, self.listView_tool_specifications)
        MainWindow.setTabOrder(self.listView_tool_specifications, self.toolButton_add_tool_specification)
        MainWindow.setTabOrder(self.toolButton_add_tool_specification, self.toolButton_remove_tool_specification)
        MainWindow.setTabOrder(self.toolButton_remove_tool_specification, self.graphicsView)
        MainWindow.setTabOrder(self.graphicsView, self.textBrowser_eventlog)
        MainWindow.setTabOrder(self.textBrowser_eventlog, self.textBrowser_process_output)
        MainWindow.setTabOrder(self.textBrowser_process_output, self.tabWidget_item_properties)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Spine Toolbox", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Design View", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.menuView.setTitle(QtWidgets.QApplication.translate("MainWindow", "View", None, -1))
        self.menuToolbars.setTitle(QtWidgets.QApplication.translate("MainWindow", "Toolbars", None, -1))
        self.menuDock_Widgets.setTitle(QtWidgets.QApplication.translate("MainWindow", "Dock widgets", None, -1))
        self.dockWidget_eventlog.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Event Log", None, -1))
        self.dockWidget_process_output.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Process Log", None, -1))
        self.dockWidget_item.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Properties", None, -1))
        self.label_no_selection.setText(QtWidgets.QApplication.translate("MainWindow", "Select a project item to view its properties", None, -1))
        self.tabWidget_item_properties.setTabText(self.tabWidget_item_properties.indexOf(self.tab_no_selection), QtWidgets.QApplication.translate("MainWindow", "No Selection", None, -1))
        self.dockWidget_julia_repl.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Julia Console", None, -1))
        self.dockWidget_project.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Project", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Items", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Tool specifications", None, -1))
        self.listView_tool_specifications.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Tool specifications available in this project</p></body></html>", None, -1))
        self.toolButton_add_tool_specification.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Create new or add an existing Tool specification to project</p></body></html>", None, -1))
        self.toolButton_remove_tool_specification.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Remove (selected) Tool specification from project</p></body></html>", None, -1))
        self.dockWidget_python_repl.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Python Console", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.actionQuit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionData_Store.setText(QtWidgets.QApplication.translate("MainWindow", "Data Store", None, -1))
        self.actionDocumentation.setText(QtWidgets.QApplication.translate("MainWindow", "Documentation", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About...", None, -1))
        self.actionAbout.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F12", None, -1))
        self.actionAdd_Data_Connection.setText(QtWidgets.QApplication.translate("MainWindow", "Add Data Connection", None, -1))
        self.actionAdd_Data_Store.setText(QtWidgets.QApplication.translate("MainWindow", "Add Data Store", None, -1))
        self.actionAdd_Tool.setText(QtWidgets.QApplication.translate("MainWindow", "Add Tool", None, -1))
        self.actionAdd_View.setText(QtWidgets.QApplication.translate("MainWindow", "Add View", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save project", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionSave_As.setText(QtWidgets.QApplication.translate("MainWindow", "Save project as...", None, -1))
        self.actionSave_As.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Duplicate project under a new name", None, -1))
        self.actionSave_As.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open project...", None, -1))
        self.actionOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionNew.setText(QtWidgets.QApplication.translate("MainWindow", "New project...", None, -1))
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
        self.actionUser_Guide.setText(QtWidgets.QApplication.translate("MainWindow", "User guide", None, -1))
        self.actionUser_Guide.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F2", None, -1))
        self.actionRestore_Dock_Widgets.setText(QtWidgets.QApplication.translate("MainWindow", "Restore Dock Widgets", None, -1))
        self.actionRestore_Dock_Widgets.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Dock all floating and/or hidden dock widgets back to main window.</p></body></html>", None, -1))
        self.actionAbout_Qt.setText(QtWidgets.QApplication.translate("MainWindow", "About Qt...", None, -1))
        self.actionAbout_Qt.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F11", None, -1))
        self.actionPackages.setText(QtWidgets.QApplication.translate("MainWindow", "Tool configuration assistant...", None, -1))
        self.actionPackages.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F5", None, -1))
        self.actionRemove_all.setText(QtWidgets.QApplication.translate("MainWindow", "Remove all", None, -1))
        self.actionRemove_all.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Remove all items project</p></body></html>", None, -1))
        self.actionExport_project_to_GraphML.setText(QtWidgets.QApplication.translate("MainWindow", "Export project to GraphML", None, -1))
        self.actionAdd_Importer.setText(QtWidgets.QApplication.translate("MainWindow", "Add Importer", None, -1))
        self.actionAdd_Importer.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add Importer", None, -1))
        self.actionGetting_started.setText(QtWidgets.QApplication.translate("MainWindow", "Getting started", None, -1))
        self.actionGetting_started.setShortcut(QtWidgets.QApplication.translate("MainWindow", "F3", None, -1))
        self.actionOpen_recent.setText(QtWidgets.QApplication.translate("MainWindow", "Open recent", None, -1))
        self.actionCopy.setText(QtWidgets.QApplication.translate("MainWindow", "Copy", None, -1))
        self.actionCopy.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+C", None, -1))
        self.actionPaste.setText(QtWidgets.QApplication.translate("MainWindow", "Paste", None, -1))
        self.actionPaste.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+V", None, -1))
        self.actionDuplicate.setText(QtWidgets.QApplication.translate("MainWindow", "Duplicate", None, -1))
        self.actionDuplicate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Duplicate selected project item", None, -1))
        self.actionDuplicate.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+D", None, -1))
        self.actionLive_tutorial.setText(QtWidgets.QApplication.translate("MainWindow", "Live tutorial", None, -1))
        self.actionLive_tutorial.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Shift+F2", None, -1))

from spinetoolbox.widgets.custom_qtextbrowser import CustomQTextBrowser
from spinetoolbox.widgets.custom_qgraphicsviews import DesignQGraphicsView
from spinetoolbox import resources_icons_rc
