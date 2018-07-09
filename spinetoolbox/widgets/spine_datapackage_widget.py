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
Widget shown to user when pressing Convert to Spine or smething like that
on Data Connection item.

:author: Manuel Marin <manuelma@kth.se>
:date:   7.7.2018
"""

import os
import shutil
import tempfile
import logging
from config import STATUSBAR_SS
from ui.spine_datapackage_form import Ui_MainWindow
from widgets.lineedit_delegate import LineEditDelegate
from widgets.custom_menus import DescriptorTreeContextMenu
from PySide2.QtWidgets import QMainWindow, QHeaderView, QMessageBox
from PySide2.QtCore import Qt, Slot, QSettings, SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem, QFont, QFontMetrics
from helpers import create_fresh_Spine_database, busy_effect
from models import MinimalTableModel
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import Session
from datapackage import Package


class SpineDatapackageWidget(QMainWindow):
    """A widget to request user's preferences for converting data
    from a datapackage into Spine data structure.

    Attributes:
        data_connection (DataConnection): Data Connection that owns this widget.
    """
    def __init__(self, parent, data_connection):
        """Initialize class."""
        super().__init__(flags=Qt.Window)
        self._parent = parent
        self._data_connection = data_connection
        self.engine = None
        self.temp_filename = None
        self.Base = None
        self.session = None
        self.ObjectClass = None
        self.Object = None
        self.RelationshipClass = None
        self.Relationship = None
        self.Parameter = None
        self.ParameterValue = None
        self.Commit = None
        self.datapackage = None
        self.object_class_name_list = None
        font = QFont("", 0)
        self.font_metric = QFontMetrics(font)
        self.max_resource_name_width = None
        self.descriptor_tree_context_menu = None
        self.current_resource_index = None
        self.resource_tables = list()
        #  Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.qsettings = QSettings("SpineProject", "Spine Toolbox datapackage form")
        # Add status bar to form
        self.ui.statusbar.setFixedHeight(20)
        self.ui.statusbar.setSizeGripEnabled(False)
        self.ui.statusbar.setStyleSheet(STATUSBAR_SS)
        # Ensure this window gets garbage-collected when closed
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.create_engine()
        if not self.create_base_and_reflect_tables():
            self.close()
            return
        self.create_session()
        self.descriptor_model = QStandardItemModel(self)
        self.descriptor_model_header = ["Key", "Value"]
        self.descriptor_model.flags = self.descriptor_model_flags
        self.descriptor_model.headerData = self.descriptor_model_header_data
        self.load_datapackage()
        self.ui.treeView_descriptor.setModel(self.descriptor_model)
        self.resource_data_model = MinimalTableModel()
        self.ui.tableView_resource_data.setModel(self.resource_data_model)
        self.ui.tableView_resource_data.horizontalHeader().\
            setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableView_resource_data.verticalHeader().\
            setSectionResizeMode(QHeaderView.ResizeToContents)
        self.connect_signals()
        self.restore_ui()

    def connect_signals(self):
        """Connect signals to slots."""
        self.ui.treeView_descriptor.expanded.connect(self.resize_treeview_descriptor)
        self.ui.treeView_descriptor.collapsed.connect(self.resize_treeview_descriptor)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionConvert.triggered.connect(self.convert_triggered)
        self.ui.actionInfer_datapackage.triggered.connect(self.infer_datapackage)
        self.ui.actionLoad_datapackage.triggered.connect(self.load_datapackage)
        self.ui.actionSave_datapackage.triggered.connect(self.save_datapackage)
        resource_data_lineedit_delegate = LineEditDelegate(self)
        resource_data_lineedit_delegate.closeEditor.connect(self.resource_data_editor_closed)
        self.ui.tableView_resource_data.setItemDelegate(resource_data_lineedit_delegate)
        self.ui.treeView_descriptor.selectionModel().currentChanged.connect(self.update_resource_table)
        self.ui.treeView_descriptor.customContextMenuRequested.\
            connect(self.show_descriptor_tree_context_menu)

    def restore_ui(self):
        """Restore UI state from previous session."""
        window_size = self.qsettings.value("mainWindow/windowSize")
        window_pos = self.qsettings.value("mainWindow/windowPosition")
        splitter_state = self.qsettings.value("mainWindow/splitterState")
        window_maximized = self.qsettings.value("mainWindow/windowMaximized", defaultValue='false')  # returns string
        if window_size:
            self.resize(window_size)
        if window_pos:
            self.move(window_pos)
        if window_maximized == 'true':
            self.setWindowState(Qt.WindowMaximized)
        if splitter_state:
            self.ui.splitter.restoreState(splitter_state)

    def create_engine(self):
        """Create engine with a fresh Spine database."""
        self.temp_filename = os.path.join(tempfile.gettempdir(), 'Spine.sqlite')
        url = "sqlite:///" + self.temp_filename
        self.engine = create_engine(url)
        create_fresh_Spine_database(self.engine)

    def create_base_and_reflect_tables(self):
        """Create base and reflect tables."""
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        try:
            self.ObjectClass = self.Base.classes.object_class
            self.Object = self.Base.classes.object
            self.RelationshipClass = self.Base.classes.relationship_class
            self.Relationship = self.Base.classes.relationship
            self.Parameter = self.Base.classes.parameter
            self.ParameterValue = self.Base.classes.parameter_value
            self.Commit = self.Base.classes.commit
            return True
        except AttributeError as e:
            self._parent.msg_error.emit("Unable to parse database in the Spine format. "
                                        " Table <b>{}</b> is missing.".format(e))
            return False

    def create_session(self):
        """Create session."""
        self.session = Session(self.engine)
        object_class_name_query = self.session.query(self.ObjectClass.name)
        self.object_class_name_list = [item.name for item in object_class_name_query]
        self.max_resource_name_width = max(self.font_metric.width(x) for x in self.object_class_name_list)

    def load_resource_data(self):
        """Load resource data into a local list of tables."""
        if not self.datapackage:
            return
        for resource in self.datapackage.resources:
            table = list()
            table.append(resource.schema.field_names)
            table.extend(resource.read(cast=False))
            self.resource_tables.append(table)

    @busy_effect
    @Slot("Boolean", name="load_datapackage")
    def load_datapackage(self, load_resource_data=True):
        """Attempt to load existing datapackage.json file in data directory."""
        file_path = os.path.join(self._data_connection.data_dir, "datapackage.json")
        if not os.path.exists(file_path):
            msg = "File 'datapackage.json' not found in {}."\
                  " Try 'Infer new datapackage' instead.".format(self._data_connection.data_dir)
            self.ui.statusbar.showMessage(msg, 5000)
            return
        msg = "Loading datapackage from {}".format(file_path)
        self.ui.statusbar.showMessage(msg)
        self.datapackage = Package(file_path)
        msg = "Datapackage loaded from {}".format(file_path)
        self.ui.statusbar.showMessage(msg, 3000)
        # self.spinify_datapackage()
        self.init_descriptor_model()
        if load_resource_data:
            self.load_resource_data()

    @busy_effect
    @Slot("Boolean", name="infer_datapackage")
    def infer_datapackage(self, load_resource_data=True):
        """Infer datapackage from CSV files in data directory."""
        data_files = self._data_connection.data_files()
        if not ".csv" in [os.path.splitext(f)[1] for f in data_files]:
            msg = ("The folder {} does not have any CSV files."
                   " Add some and try again.".format(self._data_connection.data_dir))
            self.ui.statusbar.showMessage(msg, 5000)
            return
        msg = "Inferring datapackage from {}".format(self._data_connection.data_dir)
        self.ui.statusbar.showMessage(msg)
        self.datapackage = Package(base_path = self._data_connection.data_dir)
        self.datapackage.infer(os.path.join(self._data_connection.data_dir, '*.csv'))
        msg = "Datapackage inferred from {}".format(self._data_connection.data_dir)
        self.ui.statusbar.showMessage(msg, 3000)
        # self.spinify_datapackage()
        self.init_descriptor_model()
        if load_resource_data:
            self.load_resource_data()

    @Slot(name="save_datapackage")
    def save_datapackage(self):  #TODO: handle zip as well?
        """Save datapackage.json to datadir"""
        if os.path.exists(os.path.join(self._data_connection.data_dir, "datapackage.json")):
            msg = '<b>Replacing file "datapackage.json" in "{}"</b>.'\
                  ' Are you sure?'.format(os.path.basename(self._data_connection.data_dir))
            # noinspection PyCallByClass, PyTypeChecker
            answer = QMessageBox.question(None, 'Replace datapackage.json', msg, QMessageBox.Yes, QMessageBox.No)
            if not answer == QMessageBox.Yes:
                return False
        if self.datapackage.save(os.path.join(self._data_connection.data_dir, 'datapackage.json')):
            msg = "datapackage.json saved in {}".format(self._data_connection.data_dir)
            self.ui.statusbar.showMessage(msg, 3000)
            return True
            msg = "Failed to save datapackage.json in {}".format(self._data_connection.data_dir)
            self.ui.statusbar.showMessage(msg, 5000)
        return False

    def init_descriptor_model(self):
        """Init datpackage descriptor model"""
        self.descriptor_model.clear()
        def visit(parent_item, value):
            for key,new_value in value.items():
                key_item = QStandardItem(str(key))
                key_item.setData(key, Qt.UserRole)
                value_item = None
                if isinstance(new_value, dict):
                    visit(key_item, new_value)
                elif isinstance(new_value, list):
                    visit(key_item, dict(enumerate(new_value)))
                else:
                    value_item = QStandardItem(str(new_value))
                row = list()
                row.append(key_item)
                if value_item:
                    row.append(value_item)
                parent_item.appendRow(row)
        visit(self.descriptor_model, self.datapackage.descriptor)
        self.ui.treeView_descriptor.resizeColumnToContents(0)

    def descriptor_model_flags(self, index):
        """Returns enabled flags for the given index.

        Args:
            index (QModelIndex): Index of Tool
        """
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def descriptor_model_header_data(self, section, orientation, role=Qt.DisplayRole):
        """Set headers."""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            try:
                h = self.descriptor_model_header[section]
            except IndexError:
                return None
            return h
        else:
            return None

    def find_item_in_descriptor_model(self, key_chain):
        """Find item under a chain a keys.

        Returns:
            key: the last key explored from key_chain
            item: the last item visited
        """
        key_iterator = iter(key_chain)
        item = self.descriptor_model.invisibleRootItem()
        while item.hasChildren():
            try:
                key = next(key_iterator)
            except StopIteration:
                break
            for i in range(item.rowCount()):
                child = item.child(i)
                if child.data(Qt.UserRole) == key:
                    item = child
                    break
        return key, item

    @Slot("QModelIndex", name="resize_treeview_descriptor")
    def resize_treeview_descriptor(self, index):
        self.ui.treeView_descriptor.resizeColumnToContents(0)

    @Slot("QModelIndex", "QModelIndex", name="update_resource_table")
    def update_resource_table(self, current, previous):
        """Update resource tableView and comboBox whenever a resource item is selected in the treeView."""
        index = current
        selected_resource_index = None
        while index.parent().isValid():
            if index.parent().data(Qt.UserRole) == 'resources':
                selected_resource_index = index.data(Qt.UserRole)  # resource pos in json array
                break
            index = index.parent()
        if selected_resource_index is None:
            return
        if self.current_resource_index == selected_resource_index:  # selected resource not changed
            return
        self.current_resource_index = selected_resource_index
        table = self.resource_tables[self.current_resource_index]
        self.resource_data_model.header = table[0]  # TODO: find out why this is needed
        self.resource_data_model.reset_model(table)
        self.ui.tableView_resource_data.resizeColumnsToContents()
        # Update resource name combobox
        # Disconnect signal
        n_recv = self.ui.comboBox_resource_name.receivers(SIGNAL("currentTextChanged(QString)"))
        if n_recv > 0:
            self.ui.comboBox_resource_name.currentTextChanged.disconnect(self.resource_name_changed)
        self.ui.comboBox_resource_name.clear()
        resource_name = self.datapackage.resources[self.current_resource_index].name
        self.ui.comboBox_resource_name.addItems(self.object_class_name_list)
        max_width = self.max_resource_name_width
        if resource_name not in self.object_class_name_list:
            self.ui.comboBox_resource_name.insertItem(0, resource_name + ' (unsupported)')
            self.ui.comboBox_resource_name.setCurrentIndex(0)
            width = self.font_metric.width(resource_name + ' (unsupported)')
            max_width = max(max_width, width)
        else:
            ind = self.object_class_name_list.index(resource_name)
            self.ui.comboBox_resource_name.setCurrentIndex(ind)
        # Set combobox width based on items
        self.ui.comboBox_resource_name.setMinimumWidth(max_width + 24)
        # Reconnect signal
        self.ui.comboBox_resource_name.currentTextChanged.connect(self.resource_name_changed)

    @Slot("QWidget", "QAbstractItemDelegate.EndEditHint", name="resource_data_editor_closed")
    def resource_data_editor_closed(self, editor, hint):
        """Update resource with newly edited data."""
        index = editor.index
        if not self.resource_data_model.setData(index, editor.text(), Qt.EditRole):
            return
        self.ui.tableView_resource_data.resizeColumnsToContents()
        # Update descriptor in datapackage in case a field name was modified
        if not index.row() == 0:
            return
        new_name = editor.text()
        field_index = index.column()
        resource_dict = self.datapackage.descriptor['resources'][self.current_resource_index]
        resource_dict['schema']['fields'][field_index]['name'] = new_name
        self.datapackage.commit()
        # Update descriptor model
        key_chain = ['resources', self.current_resource_index, 'schema', 'fields', field_index, 'name']
        key, item = self.find_item_in_descriptor_model(key_chain)
        if key != key_chain[-1]:
            msg = "Couldn't find field in datapackage descriptor. Something is wrong."
            self.ui.statusbar.showMessage(msg, 5000)
            return
        ind = item.index()
        sib = ind.sibling(ind.row(), 1)
        self.descriptor_model.setData(sib, new_name, Qt.EditRole)

    @Slot("str", name="resource_name_changed")
    def resource_name_changed(self, text):
        """Update descriptor with new resource name from comboBox."""
        # Update descriptor in datapackage
        self.datapackage.descriptor['resources'][self.current_resource_index]['name'] = text
        self.datapackage.commit()
        # Update descriptor in model
        key_chain = ['resources', self.current_resource_index, 'name']
        key, item = self.find_item_in_descriptor_model(key_chain)
        if key != key_chain[-1]:
            msg = "Couldn't find resource in datapackage descriptor. Something is wrong."
            self.ui.statusbar.showMessage(msg, 5000)
            return
        ind = item.index()
        sib = ind.sibling(ind.row(), 1)
        self.descriptor_model.setData(sib, text, Qt.EditRole)
        # Remove unsupported name
        ind = self.ui.comboBox_resource_name.findText("unsupported", Qt.MatchContains)
        if ind == -1:
            return
        self.ui.comboBox_resource_name.removeItem(ind)


    @Slot(name="convert_triggered")
    def convert_triggered(self):
        """Check if there are unsupported resource names, prompt the user
        and launch conversion."""
        unsupported_names = list()
        for resource in self.datapackage.resources:
            if resource.name not in self.object_class_name_list:
                unsupported_names.append(resource.name)
        if unsupported_names:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Unsupported resource names")
            text = ("The following resources have unsupported names "
                    "and will be ignored by the conversion process:<ul>")
            for name in unsupported_names:
                text += "<li>{}</li>".format(name)
            text += "</ul>"
            msg.setText(text)
            msg.setInformativeText("Do you want to convert anyway?")
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
            answer = msg.exec_()  # Show message box
            if answer == QMessageBox.Cancel:
                return
        self.convert()
        # Clean up session after converting
        try:
            self.session.query(self.Object).delete()
            self.session.query(self.RelationshipClass).delete()
            self.session.query(self.Relationship).delete()
            self.session.query(self.Parameter).delete()
            self.session.query(self.ParameterValue).delete()
            self.session.query(self.Commit).delete()
            self.session.flush()
        except Exception as e:
            msg = "Could not clean up session: {}".format(e.orig.args)
            self.ui.statusbar.showMessage(msg, 5000)

    @busy_effect
    def convert(self):
        """Convert datapackge into Spine database and save it in data directory as Spine.sqlite."""
        for j, resource in enumerate(self.datapackage.resources):
            object_class_name = resource.name
            if object_class_name not in self.object_class_name_list:
                continue
            object_class_id = self.session.query(self.ObjectClass.id).\
                filter_by(name=object_class_name).one().id
            relationship_class_id_dict = dict()
            parameter_id_dict = dict()
            for field in resource.schema.fields:
                # A field named exactly as the object_class is a primary key
                if field.name == object_class_name:
                    continue
                # Fields whose name contains a resource name are foreign keys
                # and used to create relationships
                matched = None
                for x in self.object_class_name_list:
                    if x == object_class_name:
                        continue
                    if x in field.name:
                        matched = x
                        break
                if matched:
                    # Relationship class
                    child_object_class_id = self.session.query(self.ObjectClass.id).\
                        filter_by(name=matched).one().id
                    relationship_class_name = resource.name + "_" + field.name
                    relationship_class = self.RelationshipClass(
                        commit_id=1,
                        parent_object_class_id=object_class_id,
                        child_object_class_id=child_object_class_id,
                        name=relationship_class_name
                    )
                    try:
                        self.session.add(relationship_class)
                        self.session.flush()
                        relationship_class_id_dict[field.name] = relationship_class.id
                    except DBAPIError as e:
                        msg = ("Failed to insert relationship class {0} for object class {1}: {2}".\
                            format(relationship_class_name, object_class_name, e.orig.args))
                        self.ui.statusbar.showMessage(msg, 5000)
                        self.session.rollback()
                        return
                else:
                    # Parameter
                    parameter_name = field.name
                    parameter = self.Parameter(
                        commit_id=1,
                        object_class_id=object_class_id,
                        name=parameter_name
                    )
                    try:
                        self.session.add(parameter)
                        self.session.flush()
                        parameter_id_dict[field.name] = parameter.id
                    except DBAPIError as e:
                        msg = ("Failed to insert parameter {0} for object class {1}: {2}".\
                            format(parameter_name, object_class_name, e.orig.args))
                        self.ui.statusbar.showMessage(msg, 5000)
                        self.session.rollback()
                        return
            # Iterate over resource data to create objects and parameter values
            object_id_dict = dict()
            for i, row in enumerate(self.resource_tables[j][1:]):
                row_dict = dict(zip(resource.schema.field_names, row))
                # Get object name from primery key
                if object_class_name in row_dict:
                    object_name = row_dict[object_class_name]
                else:
                    object_name = object_class_name + str(i)
                object_ = self.Object(
                    commit_id=1,
                    class_id=object_class_id,
                    name=object_name
                )
                try:
                    self.session.add(object_)
                    self.session.flush()
                    object_id = object_.id
                except DBAPIError as e:
                    msg = "Failed to insert object {0} to object class {1}: {2}".\
                        format(object_name, object_class_name, e.orig.args)
                    self.ui.statusbar.showMessage(msg, 5000)
                    self.session.rollback()
                    return
                object_id_dict[i] = object_.id
                for key, value in row_dict.items():
                    if key in parameter_id_dict:
                        parameter_id = parameter_id_dict[key]
                        parameter_value = self.ParameterValue(
                            commit_id=1,
                            object_id=object_id,
                            parameter_id=parameter_id,
                            value=value
                        )
                        try:
                            self.session.add(parameter_value)
                            self.session.flush()
                            object_id = object_.id
                        except DBAPIError as e:
                            msg = "Failed to insert parameter value {0} for object {1} of class {2}: {3}".\
                                format(key, object_name, object_class_name, e.orig.args)
                            self.ui.statusbar.showMessage(msg, 5000)
                            self.session.rollback()
                            return
            # Iterate over resource data (again) to create relationships
            for i, row in enumerate(self.resource_tables[j][1:]):
                row_dict = dict(zip(resource.schema.field_names, row))
                if object_class_name in row_dict:
                    parent_object_name = row_dict[object_class_name]
                else:
                    parent_object_name = object_class_name + str(i)
                parent_object_id = object_id_dict[i]
                for key, value in row_dict.items():
                    if key in relationship_class_id_dict:
                        relationship_class_id = relationship_class_id_dict[key]
                        child_object_name = value
                        child_object = self.session.query(self.Object.id).\
                            filter_by(name=child_object_name).one_or_none()
                        relationship_name = parent_object_name + key + child_object_name
                        if child_object is None:
                            msg = "Couldn't find object {} to create relationship {}".\
                                format(child_object_name, relationship_name)
                            self.ui.statusbar.showMessage(msg, 5000)
                            self.session.rollback()
                            return
                        relationship = self.Relationship(
                            commit_id=1,
                            class_id=relationship_class_id,
                            parent_object_id=parent_object_id,
                            child_object_id=child_object.id,
                            name=relationship_name
                        )
                        try:
                            self.session.add(relationship)
                            self.session.flush()
                            object_id = object_.id
                        except DBAPIError as e:
                            msg = "Failed to insert relationship {0} for object {1} of class {2}: {3}".\
                                format(key, parent_object_name, object_class_name, e.orig.args)
                            self.ui.statusbar.showMessage(msg, 5000)
                            self.session.rollback()
                            return
        self.session.commit()
        target_filename = os.path.join(self._data_connection.data_dir, 'Spine.sqlite')
        try:
            shutil.copy(self.temp_filename, target_filename)
        except OSError:
            msg = "Conversion failed. [OSError] Unable to copy file from temporary location."
            self.ui.statusbar.showMessage(msg, 5000)
            return
        msg = "Conversion finished. File 'Spine.sqlite' saved in {}".format(self._data_connection.data_dir)
        self.ui.statusbar.showMessage(msg, 5000)


    @Slot("QPoint", name="show_descriptor_tree_context_menu")
    def show_descriptor_tree_context_menu(self, pos):
        """Context menu for descriptor treeview.

        Args:
            pos (QPoint): Mouse position
        """
        index = self.ui.treeView_descriptor.indexAt(pos)
        global_pos = self.ui.treeView_descriptor.viewport().mapToGlobal(pos)
        self.descriptor_tree_context_menu = DescriptorTreeContextMenu(self, global_pos, index)
        option = self.descriptor_tree_context_menu.get_action()
        if option == "Expand all children":
            self.ui.treeView_descriptor.expand(index)
            if not self.descriptor_model.hasChildren(index):
                return
            for i in range(self.descriptor_model.rowCount(index)):
                child_index = self.descriptor_model.index(i, 0, index)
                self.ui.treeView_descriptor.expand(child_index)
        elif option == "Collapse all children":
            self.ui.treeView_descriptor.collapse(index)
            if not self.descriptor_model.hasChildren(index):
                return
            for i in range(self.descriptor_model.rowCount(index)):
                child_index = self.descriptor_model.index(i, 0, index)
                self.ui.treeView_descriptor.collapse(child_index)

    def closeEvent(self, event=None):
        """Handle close window.

        Args:
            event (QEvent): Closing event if 'X' is clicked.
        """
        # save qsettings
        self.qsettings.setValue("mainWindow/splitterState", self.ui.splitter.saveState())
        self.qsettings.setValue("mainWindow/windowSize", self.size())
        self.qsettings.setValue("mainWindow/windowPosition", self.pos())
        if self.windowState() == Qt.WindowMaximized:
            self.qsettings.setValue("mainWindow/windowMaximized", True)
        else:
            self.qsettings.setValue("mainWindow/windowMaximized", False)
        # close sql session
        if self.session:
            self.session.rollback()
            self.session.close()
        if self.engine:
            self.engine.dispose()
        if self.temp_filename:
            try:
                os.remove(self.temp_filename)
            except OSError:
                pass
        if event:
            event.accept()