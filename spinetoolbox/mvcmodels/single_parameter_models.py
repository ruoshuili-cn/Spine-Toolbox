######################################################################################################################
# Copyright (C) 2017 - 2019 Spine project consortium
# This file is part of Spine Toolbox.
# Spine Toolbox is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option)
# any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General
# Public License for more details. You should have received a copy of the GNU Lesser General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
######################################################################################################################

"""
Single models for parameter definitions and values (as 'for a single entity').

:authors: M. Marin (KTH)
:date:   28.6.2019
"""

from PySide2.QtCore import Qt
from ..mvcmodels.filled_parameter_models import FilledParameterModel
from ..mvcmodels.parameter_mixins import FillInParameterNameMixin, FillInValueListIdMixin, MakeParameterTagMixin


class SingleParameterModel(FilledParameterModel):
    """A parameter model for a single entity class to go in a CompoundParameterModel.
    Provides methods to associate the model to an entity class as well as
    to filter entities within the class.
    """

    def __init__(self, *args, **kwargs):
        """Init class.

        Args:
            parent (CompoundParameterModel): the parent object
            header (list): list of field names for the header
        """
        super().__init__(*args, **kwargs)
        self._auto_filter = dict()
        self._selected_param_def_ids = set()

    @property
    def item_type(self):
        raise NotImplementedError()

    @property
    def parameter_definition_id_key(self):
        return {"parameter definition": "id", "parameter value": "parameter_id"}[self.item_type]

    @property
    def json_fields(self):
        return {"parameter definition": ["default_value"], "parameter value": ["value"]}[self.item_type]

    @property
    def entity_class_id(self):
        """Returns the associated entity class id."""
        raise NotImplementedError()

    @property
    def can_be_filtered(self):
        return True

    def _filter_accepts_item(self, item, ignored_columns=None):
        return self._main_filter_accepts_item(item) and self._auto_filter_accepts_item(
            item, ignored_columns=ignored_columns
        )

    def _main_filter_accepts_item(self, item):
        """Applies the main filter, defined by the selections in the grand parent."""
        if self._selected_param_def_ids:
            return item[self.parameter_definition_id_key] in self._selected_param_def_ids
        return True

    def _auto_filter_accepts_item(self, item, ignored_columns=None):
        """Applies the autofilter, defined by the autofilter drop down menu."""
        if ignored_columns is None:
            ignored_columns = []
        for column, values in self._auto_filter.items():
            if column in ignored_columns:
                continue
            if item[self.header[column]] in values:
                return False
        return True

    def accepted_rows(self, ignored_columns=None):
        """Returns a list of accepted rows, for convenience."""
        return [
            row
            for row in range(self.rowCount())
            if self._filter_accepts_item(self._db_item_at_row(row), ignored_columns=ignored_columns)
        ]

    def _db_item_at_row(self, row):
        return self.db_mngr.get_item(self.db_map, self.item_type, self._main_data[row])


class SingleObjectParameterMixin:
    """Associates a parameter model with a single object class."""

    def __init__(self, parent, header, db_mngr, db_map, object_class_id, *args, **kwargs):
        """Init class.

        Args:
            object_class_id (int): the id of the object class
        """
        super().__init__(parent, header, db_mngr, db_map, *args, **kwargs)
        self.object_class_id = object_class_id

    @property
    def entity_class_id(self):
        return self.object_class_id

    def data(self, index, role=Qt.DisplayRole):
        """Return data for given index and role.
        Paint the object class icon next to the name.
        """
        if role == Qt.DecorationRole and self.header[index.column()] == "object_class_name":
            return self.db_mngr.entity_class_icon(self.db_map, "object class", self.object_class_id)
        return super().data(index, role)


class SingleRelationshipParameterMixin:
    """Associates a parameter model with a single relationship class."""

    def __init__(self, parent, header, db_mngr, db_map, relationship_class_id, *args, **kwargs):
        """Init class.

        Args:
            relationship_class_id (int): the id of the relationship class
        """
        super().__init__(parent, header, db_mngr, db_map, *args, **kwargs)
        self.relationship_class_id = relationship_class_id

    @property
    def entity_class_id(self):
        return self.relationship_class_id

    def data(self, index, role=Qt.DisplayRole):
        """Return data for given index and role.
        Paint the object class icon next to the name.
        """
        if role == Qt.DecorationRole and self.header[index.column()] == "relationship_class_name":
            return self.db_mngr.entity_class_icon(self.db_map, "relationship class", self.relationship_class_id)
        return super().data(index, role)


class SingleObjectParameterValueMixin:
    """Filters objects within a class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._selected_object_ids = {}

    def _main_filter_accepts_item(self, item):
        """Reimplemented to filter objects."""
        if not super()._main_filter_accepts_item(item):
            return False
        if self._selected_object_ids:
            return item["object_id"] in self._selected_object_ids
        return True


class SingleRelationshipParameterValueMixin:
    """Filters relationships within a class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._selected_relationship_ids = {}

    def _main_filter_accepts_item(self, item):
        """Reimplemented to filter relationships and objects."""
        if not super()._main_filter_accepts_item(item):
            return False
        if self._selected_relationship_ids:
            return item["relationship_id"] in self._selected_relationship_ids
        return True


class SingleParameterDefinitionModel(
    FillInParameterNameMixin, FillInValueListIdMixin, MakeParameterTagMixin, SingleParameterModel
):
    """A parameter definition model for a single entity class."""

    @property
    def item_type(self):
        return "parameter definition"

    def update_items_in_db(self, items):
        """Update items in db.

        Args:
            item (list): dictionary-items
        """
        self.build_lookup_dictionary({self.db_map: items})
        param_defs = list()
        param_def_tags = list()
        for item in items:
            param_def = self._convert_to_db(item, self.db_map)
            param_def_tag = self._make_parameter_definition_tag(item, self.db_map)
            if param_def:
                param_defs.append(param_def)
            if param_def_tag:
                param_def_tags.append(param_def_tag)
        if param_def_tags:
            self.db_mngr.set_parameter_definition_tags({self.db_map: param_def_tags})
        if param_defs:
            self.db_mngr.update_parameter_definitions({self.db_map: param_defs})


class SingleParameterValueModel(SingleParameterModel):
    """A parameter value model for a single entity class."""

    @property
    def item_type(self):
        return "parameter value"

    def update_items_in_db(self, items):
        """Update items in db.

        Args:
            item (list): dictionary-items
        """
        self.db_mngr.update_parameter_values({self.db_map: items})


class SingleObjectParameterDefinitionModel(SingleObjectParameterMixin, SingleParameterDefinitionModel):
    """An object parameter definition model for a single object class."""

    fixed_fields = ["object_class_name", "database"]

    def fetch_data(self):
        """Returns object parameter definition ids."""
        return [
            x["id"]
            for x in self.db_mngr.get_object_parameter_definitions(self.db_map, object_class_id=self.object_class_id)
        ]


class SingleRelationshipParameterDefinitionModel(SingleRelationshipParameterMixin, SingleParameterDefinitionModel):
    """A relationship parameter definition model for a single relationship class."""

    fixed_fields = ["relationship_class_name", "object_class_name_list", "database"]

    def fetch_data(self):
        """Returns relationship parameter definition ids."""
        return [
            x["id"]
            for x in self.db_mngr.get_relationship_parameter_definitions(
                self.db_map, relationship_class_id=self.relationship_class_id
            )
        ]


class SingleObjectParameterValueModel(
    SingleObjectParameterMixin, SingleObjectParameterValueMixin, SingleParameterValueModel
):
    """An object parameter value model for a single object class."""

    fixed_fields = ["object_class_name", "object_name", "parameter_name", "database"]

    def fetch_data(self):
        """Returns object parameter value ids."""
        return [
            x["id"] for x in self.db_mngr.get_object_parameter_values(self.db_map, object_class_id=self.object_class_id)
        ]


class SingleRelationshipParameterValueModel(
    SingleRelationshipParameterMixin, SingleRelationshipParameterValueMixin, SingleParameterValueModel
):
    """A relationship parameter value model for a single relationship class."""

    fixed_fields = ["relationship_class_name", "object_name_list", "parameter_name", "database"]

    def fetch_data(self):
        """Returns relationship parameter value ids."""
        return [
            x["id"]
            for x in self.db_mngr.get_relationship_parameter_values(
                self.db_map, relationship_class_id=self.relationship_class_id
            )
        ]
