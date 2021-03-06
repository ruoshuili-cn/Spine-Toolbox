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

"""
Models to represent entities in a tree.

:authors: P. Vennström (VTT), M. Marin (KTH)
:date:   11.3.2019
"""
from PySide2.QtCore import Qt, QModelIndex
from .entity_tree_item import ObjectTreeRootItem, RelationshipTreeRootItem
from ...mvcmodels.minimal_tree_model import MinimalTreeModel, TreeItem


class EntityTreeModel(MinimalTreeModel):
    """Base class for all entity tree models."""

    def __init__(self, parent, db_mngr, *db_maps):
        """Init class.

        Args:
            parent (DataStoreForm)
            db_mngr (SpineDBManager): A manager for the given db_maps
            db_maps (iter): DiffDatabaseMapping instances
        """
        super().__init__(parent)
        self.db_mngr = db_mngr
        self.db_maps = db_maps
        self._root_item = None
        self.active_member_indexes = dict()

    @property
    def root_item_type(self):
        """Implement in subclasses to create a model specific to any entity type."""
        raise NotImplementedError()

    @property
    def root_item(self):
        return self._root_item

    @property
    def root_index(self):
        return self.index_from_item(self._root_item)

    def build_tree(self):
        """Builds tree."""
        self.beginResetModel()
        self._invisible_root_item = TreeItem(self)
        self.endResetModel()
        self._root_item = self.root_item_type(self, dict.fromkeys(self.db_maps))
        self._invisible_root_item.append_children(self._root_item)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        item = self.item_from_index(index)
        if index.column() == 0:
            if role == Qt.DecorationRole:
                return item.display_icon
            if role == Qt.DisplayRole:
                return item.display_data
            if role == Qt.EditRole:
                return item.edit_data
        return item.data(index.column(), role)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return ("name", "database")[section]
        return None

    def find_items(self, db_map, path_prefix, parent_items=(), fetch=False):
        """Returns items at given path prefix.
        """
        if not parent_items:
            # Start from the root node
            parent_items = [self.root_item]
        for id_ in path_prefix:
            parent_items = [
                child for parent_item in parent_items for child in parent_item.find_children_by_id(db_map, id_)
            ]
            if fetch:
                for parent_item in parent_items:
                    parent = self.index_from_item(parent_item)
                    if self.canFetchMore(parent):
                        self.fetchMore(parent)
        return parent_items

    def is_active_member_index(self, index):
        return index in self.active_member_indexes.get(index.parent(), set())

    def set_active_member_indexes(self, indexes):
        self.active_member_indexes.clear()
        for ind in indexes:
            self.active_member_indexes.setdefault(ind.parent(), set()).add(ind)
        self.emit_data_changed_for_column(0, self.active_member_indexes)

    def emit_data_changed_for_column(self, column, parents):
        for parent in parents:
            top_left = self.index(0, column, parent)
            bottom_right = self.index(self.rowCount(parent), column, parent)
            self.dataChanged.emit(top_left, bottom_right)


class ObjectTreeModel(EntityTreeModel):
    """An 'object-oriented' tree model."""

    @property
    def root_item_type(self):
        return ObjectTreeRootItem

    def _parent_object_data(self, db_map_data):
        """Takes given object data and returns the same data keyed by parent tree-item.

        Args:
            db_map_data (dict): maps DiffDatabaseMapping instances to list of items as dict

        Returns:
            dict: maps parent tree-items to DiffDatabaseMapping instances to list of item ids
        """
        result = dict()
        for db_map, items in db_map_data.items():
            # Group items by class id
            d = dict()
            for item in items:
                d.setdefault(item["class_id"], dict())[item["id"]] = None
            for class_id, ids in d.items():
                # Find the parents corresponding to this class id and put them in the result
                for parent_item in self.find_items(db_map, (class_id,)):
                    result.setdefault(parent_item, {})[db_map] = list(ids.keys())
        return result

    def _parent_relationship_class_data(self, db_map_data):
        """Takes given relationship class data and returns the same data keyed by parent tree-item.

        Args:
            db_map_data (dict): maps DiffDatabaseMapping instances to list of items as dict

        Returns:
            dict: maps parent tree-items to DiffDatabaseMapping instances to list of item ids
        """
        result = dict()
        for db_map, items in db_map_data.items():
            d = dict()
            for item in items:
                for object_class_id in item["object_class_id_list"].split(","):
                    d.setdefault(int(object_class_id), dict())[item["id"]] = None
            for object_class_id, ids in d.items():
                for parent_item in self.find_items(db_map, (object_class_id, None)):
                    result.setdefault(parent_item, {})[db_map] = list(ids.keys())
        return result

    def _parent_relationship_data(self, db_map_data):
        """Takes given relationship data and returns the same data keyed by parent tree-item.

        Args:
            db_map_data (dict): maps DiffDatabaseMapping instances to list of items as dict

        Returns:
            dict: maps parent tree-items to DiffDatabaseMapping instances to list of item ids
        """
        result = dict()
        for db_map, items in db_map_data.items():
            d = dict()
            for item in items:
                d.setdefault(item["class_id"], dict())[item["id"]] = None
            for class_id, ids in d.items():
                for parent_item in self.find_items(db_map, (None, None, class_id)):
                    result.setdefault(parent_item, {})[db_map] = list(ids.keys())
        return result

    def _parent_entity_group_data(self, db_map_data):
        """Takes given entity group data and returns the same data keyed by parent tree-item.

        Args:
            db_map_data (dict): maps DiffDatabaseMapping instances to list of items as dict

        Returns:
            dict: maps parent tree-items to DiffDatabaseMapping instances to list of item ids
        """
        result = dict()
        for db_map, items in db_map_data.items():
            d = dict()
            for item in items:
                d.setdefault(item["entity_class_id"], dict())[item["entity_id"]] = None
            for class_id, ids in d.items():
                for parent_item in self.find_items(db_map, (class_id,)):
                    result.setdefault(parent_item, {})[db_map] = list(ids.keys())
        return result

    def add_object_classes(self, db_map_data):
        db_map_ids = {db_map: {x["id"] for x in data} for db_map, data in db_map_data.items()}
        self.root_item.append_children_by_id(db_map_ids)

    def add_objects(self, db_map_data):
        for parent_item, db_map_ids in self._parent_object_data(db_map_data).items():
            parent_item.append_children_by_id(db_map_ids)

    def add_relationship_classes(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_class_data(db_map_data).items():
            parent_item.append_children_by_id(db_map_ids)

    def add_relationships(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_data(db_map_data).items():
            parent_item.append_children_by_id(db_map_ids)

    def raise_entity_groups(self, db_map_data):
        for parent_item, db_map_ids in self._parent_entity_group_data(db_map_data).items():
            parent_item.raise_group_children_by_id(db_map_ids)

    def remove_object_classes(self, db_map_data):
        db_map_ids = {db_map: {x["id"] for x in data} for db_map, data in db_map_data.items()}
        self.root_item.remove_children_by_id(db_map_ids)

    def remove_objects(self, db_map_data):
        for parent_item, db_map_ids in self._parent_object_data(db_map_data).items():
            parent_item.remove_children_by_id(db_map_ids)

    def remove_relationship_classes(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_class_data(db_map_data).items():
            parent_item.remove_children_by_id(db_map_ids)

    def remove_relationships(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_data(db_map_data).items():
            parent_item.remove_children_by_id(db_map_ids)

    def update_object_classes(self, db_map_data):
        db_map_ids = {db_map: {x["id"] for x in data} for db_map, data in db_map_data.items()}
        self.root_item.update_children_by_id(db_map_ids)

    def update_objects(self, db_map_data):
        for parent_item, db_map_ids in self._parent_object_data(db_map_data).items():
            parent_item.update_children_by_id(db_map_ids)

    def update_relationship_classes(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_class_data(db_map_data).items():
            parent_item.update_children_by_id(db_map_ids)

    def update_relationships(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_data(db_map_data).items():
            parent_item.update_children_by_id(db_map_ids)

    def find_next_relationship_index(self, index):
        """Find and return next ocurrence of relationship item."""
        # Mildly insane? But I can't think of something better now
        if not index.isValid():
            return
        rel_item = self.item_from_index(index)
        if not rel_item.item_type == "relationship":
            return
        # Get all ancestors
        rel_cls_item = rel_item.parent_item
        obj_item = rel_cls_item.parent_item
        # Get data from ancestors
        # TODO: Is it enough to just use the first db_map?
        db_map = rel_item.first_db_map
        rel_data = rel_item.db_map_data(db_map)
        rel_cls_data = rel_cls_item.db_map_data(db_map)
        obj_data = obj_item.db_map_data(db_map)
        # Get specific data for our searches
        rel_cls_id = rel_cls_data['id']
        obj_id = obj_data['id']
        object_ids = list(reversed([int(id_) for id_ in rel_data['object_id_list'].split(",")]))
        object_class_ids = list(reversed([int(id_) for id_ in rel_cls_data['object_class_id_list'].split(",")]))
        # Find position in the relationship of the (grand parent) object,
        # then use it to determine object class and object id to look for
        pos = object_ids.index(obj_id) - 1
        object_id = object_ids[pos]
        object_class_id = object_class_ids[pos]
        # Return first node that passes all cascade fiters
        for parent_item in self.find_items(db_map, (object_class_id, object_id, rel_cls_id), fetch=True):
            for item in parent_item.find_children(lambda child: child.display_id == rel_item.display_id):
                return self.index_from_item(item)
        return None


class RelationshipTreeModel(EntityTreeModel):
    """A relationship-oriented tree model."""

    @property
    def root_item_type(self):
        return RelationshipTreeRootItem

    def _parent_relationship_data(self, db_map_data):
        """Takes given relationship data and returns the same data keyed by parent tree-item.

        Args:
            db_map_data (dict): maps DiffDatabaseMapping instances to list of items as dict

        Returns:
            dict: maps parent tree-items to DiffDatabaseMapping instances to list of item ids
        """
        result = dict()
        for db_map, items in db_map_data.items():
            d = dict()
            for item in items:
                d.setdefault(item["class_id"], dict())[item["id"]] = None
            for class_id, ids in d.items():
                for parent_item in self.find_items(db_map, (class_id,)):
                    result.setdefault(parent_item, {})[db_map] = list(ids.keys())
        return result

    def add_relationship_classes(self, db_map_data):
        db_map_ids = {db_map: {x["id"] for x in data} for db_map, data in db_map_data.items()}
        self.root_item.append_children_by_id(db_map_ids)

    def add_relationships(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_data(db_map_data).items():
            parent_item.append_children_by_id(db_map_ids)

    def remove_relationship_classes(self, db_map_data):
        db_map_ids = {db_map: {x["id"] for x in data} for db_map, data in db_map_data.items()}
        self.root_item.remove_children_by_id(db_map_ids)

    def remove_relationships(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_data(db_map_data).items():
            parent_item.remove_children_by_id(db_map_ids)

    def update_relationship_classes(self, db_map_data):
        db_map_ids = {db_map: {x["id"] for x in data} for db_map, data in db_map_data.items()}
        self.root_item.update_children_by_id(db_map_ids)

    def update_relationships(self, db_map_data):
        for parent_item, db_map_ids in self._parent_relationship_data(db_map_data).items():
            parent_item.update_children_by_id(db_map_ids)
