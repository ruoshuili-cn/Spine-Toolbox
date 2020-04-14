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
Contains ExecutableItem, a project item's counterpart in execution as well as support utilities.

:authors: A. Soininen (VTT)
:date:   30.3.2020
"""

from spine_engine import ExecutionDirection


class ExecutableItem:
    def __init__(self, name, logger):
        self._name = name
        self._logger = logger

    @property
    def name(self):
        return self._name

    def execute(self, resources, direction):
        """
        Executes this item in the given direction using the given resources and returns a boolean
        indicating the outcome.

        Subclasses need to implement _execute_forward and _execute_backward to do the appropriate work
        in each direction.

        Args:
            resources (list): a list of ProjectItemResources available for execution
            direction (ExecutionDirection): direction of execution

        Returns:
            bool: True if execution succeeded, False otherwise
        """
        if direction == ExecutionDirection.FORWARD:
            self._logger.msg.emit("")
            self._logger.msg.emit(f"Executing {self.item_type()} <b>{self._name}</b>")
            self._logger.msg.emit("***")
            return self._execute_forward(resources)
        return self._execute_backward(resources)

    @staticmethod
    def item_type():
        """Returns the item's type identifier string."""
        raise NotImplementedError()

    def output_resources(self, direction):
        """
        Returns output resources in the given direction.

        Subclasses need to implement _output_resources_backward and/or _output_resources_forward
        if they want to provide resources in any direction.

        Args:
            direction (ExecutionDirection): Direction where output resources are passed

        Returns:
            a list of ProjectItemResources
        """
        return {
            ExecutionDirection.BACKWARD: self._output_resources_backward,
            ExecutionDirection.FORWARD: self._output_resources_forward,
        }[direction]()

    def stop_execution(self):
        """Stops executing this View."""
        self._logger.msg.emit(f"Stopping {self._name}")

    # pylint: disable=no-self-use
    def _execute_forward(self, resources):
        """
        Executes this item in the forward direction.

        The default implementation just returns True.

        Args:
            resources (list): a list of ProjectItemResources available for execution

        Returns:
            bool: True if execution succeeded, False otherwise
        """
        return True

    # pylint: disable=no-self-use
    def _execute_backward(self, resources):
        """
        Executes this item in the backward direction.

        The default implementation just returns True.

        Args:
            resources (list): a list of ProjectItemResources available for execution

        Returns:
            bool: True if execution succeeded, False otherwise
        """
        return True

    # pylint: disable=no-self-use
    def _output_resources_forward(self):
        """
        Returns output resources for forward execution.

        The default implementation returns an empty list.

        Returns:
            a list of ProjectItemResources
        """
        return list()

    # pylint: disable=no-self-use
    def _output_resources_backward(self):
        """
        Returns output resources for backward execution.

        The default implementation returns an empty list.

        Returns:
            a list of ProjectItemResources
        """
        return list()