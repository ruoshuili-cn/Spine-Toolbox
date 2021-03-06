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
Classes for custom context menus and pop-up menus.

:author: P. Savolainen (VTT)
:date:   9.1.2018
"""

from spinetoolbox.widgets.custom_menus import CustomContextMenu


class ViewPropertiesContextMenu(CustomContextMenu):
    """Context menu class for the references tree view of the View project item properties."""

    def __init__(self, parent, position, index):
        """

        Args:
            parent (QWidget): Parent for menu widget (ToolboxUI)
            position (QPoint): Position on screen
            index (QModelIndex): Index of item that requested the context-menu
        """
        super().__init__(parent, position)
        if not index.isValid():
            # If no item at index
            return
        self.add_action("Open view")
