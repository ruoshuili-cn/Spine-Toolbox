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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

"""
Widget for controlling user settings.

:author: Pekka Savolainen <pekka.t.savolainen@vtt.fi>
:date:   17.1.2018
"""

import logging
import os
from PySide2.QtWidgets import QWidget, QStatusBar, QFileDialog
from PySide2.QtCore import Slot, Qt
import ui.settings
from config import DEFAULT_PROJECT_DIR, STATUSBAR_SS, SETTINGS_SS, \
    GAMS_EXECUTABLE, GAMSIDE_EXECUTABLE, JULIA_EXECUTABLE
from helpers import blocking_updates


class SettingsWidget(QWidget):
    """ A widget to change user's preferred settings.

    Attributes:
        parent (QObject): Parent widget.
        configs (ConfigurationParser): Configuration object
    """
    def __init__(self, parent, configs, project):
        """ Initialize class. """
        super().__init__(f=Qt.Window)
        self._parent = parent  # QWidget parent
        self._configs = configs
        self._project = project
        # Set up the user interface from Designer.
        self.ui = ui.settings.Ui_SettingsForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        # Ensure this window gets garbage-collected when closed
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.statusbar = QStatusBar(self)
        self.statusbar.setFixedHeight(20)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setStyleSheet(STATUSBAR_SS)
        self.ui.horizontalLayout_statusbar_placeholder.addWidget(self.statusbar)
        self.setStyleSheet(SETTINGS_SS)
        self.ui.pushButton_ok.setDefault(True)
        self._mousePressPos = None
        self._mouseReleasePos = None
        self._mouseMovePos = None
        self.connect_signals()
        self.read_settings()
        self.read_project_settings()

    def connect_signals(self):
        """ Connect PyQt signals. """
        self.ui.pushButton_ok.clicked.connect(self.ok_clicked)
        self.ui.pushButton_cancel.clicked.connect(self.close)
        self.ui.pushButton_browse_gams.clicked.connect(self.browse_gams_path)
        self.ui.pushButton_browse_julia.clicked.connect(self.browse_julia_path)

    @Slot(name="browse_gams_path")
    def browse_gams_path(self):
        """Open file browser where user can select the directory of
        GAMS that the user wants to use."""
        # noinspection PyCallByClass, PyTypeChecker, PyArgumentList
        func = blocking_updates(self._parent.ui.graphicsView, QFileDialog.getExistingDirectory)
        answer = func(self, 'Select GAMS Directory', os.path.abspath('C:\\'))
        if answer == '':  # Cancel button clicked
            return
        selected_path = os.path.abspath(answer)
        gams_path = os.path.join(selected_path, GAMS_EXECUTABLE)
        gamside_path = os.path.join(selected_path, GAMSIDE_EXECUTABLE)
        if not os.path.isfile(gams_path) and not os.path.isfile(gamside_path):
            self.statusbar.showMessage("gams.exe and gamside.exe not found in selected directory", 10000)
            self.ui.lineEdit_gams_path.setText("")
            return
        else:
            self.statusbar.showMessage("Selected directory is valid GAMS directory", 10000)
            self.ui.lineEdit_gams_path.setText(selected_path)
        return

    @Slot(name="browse_julia_path")
    def browse_julia_path(self):
        """Open file browser where user can select the path to wanted Julia version."""
        # noinspection PyCallByClass, PyTypeChecker, PyArgumentList
        func = blocking_updates(self._parent.ui.graphicsView, QFileDialog.getExistingDirectory)
        answer = func(self, 'Select Julia Directory', os.path.abspath('C:\\'))
        if answer == '':  # Cancel button clicked
            return
        selected_path = os.path.abspath(answer)
        julia_path = os.path.join(selected_path, JULIA_EXECUTABLE)
        if not os.path.isfile(julia_path):
            self.statusbar.showMessage("julia.exe not found in selected directory", 10000)
            self.ui.lineEdit_julia_path.setText("")
            return
        else:
            self.statusbar.showMessage("Selected directory is valid Julia directory", 10000)
            self.ui.lineEdit_julia_path.setText(selected_path)
        return

    def read_settings(self):
        """Read current settings from config object and update UI to show them."""
        open_previous_project = self._configs.getboolean("settings", "open_previous_project")
        show_exit_prompt = self._configs.getboolean("settings", "show_exit_prompt")
        logging_level = self._configs.get("settings", "logging_level")
        proj_dir = self._configs.get("settings", "project_directory")
        datetime = self._configs.getboolean("settings", "datetime")
        gams_path = self._configs.get("settings", "gams_path")
        use_repl = self._configs.getboolean("settings", "use_repl")
        julia_path =self._configs.get("settings", "julia_path")
        if open_previous_project:
            self.ui.checkBox_open_previous_project.setCheckState(Qt.Checked)
        if show_exit_prompt:
            self.ui.checkBox_exit_prompt.setCheckState(Qt.Checked)
        if logging_level == '2':
            self.ui.checkBox_debug_messages.setCheckState(Qt.Checked)
        else:
            self.ui.checkBox_debug_messages.setCheckState(Qt.Unchecked)
        if datetime:
            self.ui.checkBox_datetime.setCheckState(Qt.Checked)
        if not proj_dir:
            proj_dir = DEFAULT_PROJECT_DIR
        self.ui.lineEdit_project_dir.setText(proj_dir)
        self.ui.lineEdit_gams_path.setText(gams_path)
        if use_repl:
            self.ui.checkBox_use_repl.setCheckState(Qt.Checked)
        self.ui.lineEdit_julia_path.setText(julia_path)

    def read_project_settings(self):
        """Read project settings from config object and update settings widgets accordingly."""
        if self._project:
            self.ui.lineEdit_project_name.setText(self._project.name)
            self.ui.textEdit_project_description.setText(self._project.description)

    @Slot(name='ok_clicked')
    def ok_clicked(self):
        """Get selections and save them to conf file."""
        a = int(self.ui.checkBox_open_previous_project.checkState())
        b = int(self.ui.checkBox_exit_prompt.checkState())
        c = str(int(self.ui.checkBox_debug_messages.checkState()))
        d = int(self.ui.checkBox_datetime.checkState())
        # Check that GAMS directory is valid. Set it empty if not.
        gams_path = self.ui.lineEdit_gams_path.text()
        if not gams_path == "":  # Skip this if using GAMS in system path
            gams_exe_path = os.path.join(gams_path, GAMS_EXECUTABLE)
            gamside_exe_path = os.path.join(gams_path, GAMSIDE_EXECUTABLE)
            if not os.path.isfile(gams_exe_path) and not os.path.isfile(gamside_exe_path):
                self.statusbar.showMessage("GAMS executables not found in selected directory", 10000)
                return
        e = int(self.ui.checkBox_use_repl.checkState())
        # Check that Julia directory is valid. Set it empty if not.
        julia_path = self.ui.lineEdit_julia_path.text()
        if not julia_path == "":  # Skip this if using Julia in system path
            julia_exe_path = os.path.join(julia_path, JULIA_EXECUTABLE)
            if not os.path.isfile(julia_exe_path):
                self.statusbar.showMessage("Julia executable not found in selected directory", 10000)
                return
        # Write to config object
        self._configs.setboolean("settings", "open_previous_project", a)
        self._configs.setboolean("settings", "show_exit_prompt", b)
        self._configs.set("settings", "logging_level", c)
        self._configs.setboolean("settings", "datetime", d)
        self._configs.set("settings", "gams_path", gams_path)
        self._configs.setboolean("settings", "use_repl", e)
        self._configs.set("settings", "julia_path", julia_path)
        # Set logging level
        self._parent.set_debug_level(c)
        # Update project settings
        self.update_project_settings()
        self._configs.save()
        self.close()

    def update_project_settings(self):
        """Update project settings when Ok has been clicked."""
        if not self._project:
            return
        save = False
        if not self._project.description == self.ui.textEdit_project_description.toPlainText():
            # Set new project description
            self._project.set_description(self.ui.textEdit_project_description.toPlainText())
            save = True
        if save:
            logging.debug("Project settings changed. Saving project.")
            self._parent.save_project()

    def keyPressEvent(self, e):
        """Close settings form when escape key is pressed.

        Args:
            e (QKeyEvent): Received key press event.
        """
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event=None):
        """Handle close window.

        Args:
            event (QEvent): Closing event if 'X' is clicked.
        """
        if event:
            event.accept()

    def mousePressEvent(self, e):
        """Save mouse position at the start of dragging.

        Args:
            e (QMouseEvent): Mouse event
        """
        self._mousePressPos = e.globalPos()
        self._mouseMovePos = e.globalPos()
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        """Save mouse position at the end of dragging.

        Args:
            e (QMouseEvent): Mouse event
        """
        if self._mousePressPos is not None:
            self._mouseReleasePos = e.globalPos()
            moved = self._mouseReleasePos - self._mousePressPos
            if moved.manhattanLength() > 3:
                e.ignore()
                return

    def mouseMoveEvent(self, e):
        """Moves the window when mouse button is pressed and mouse cursor is moved.

        Args:
            e (QMouseEvent): Mouse event
        """
        # logging.debug("MouseMoveEvent at pos:%s" % e.pos())
        # logging.debug("MouseMoveEvent globalpos:%s" % e.globalPos())
        currentpos = self.pos()
        globalpos = e.globalPos()
        diff = globalpos - self._mouseMovePos
        newpos = currentpos + diff
        self.move(newpos)
        self._mouseMovePos = globalpos
