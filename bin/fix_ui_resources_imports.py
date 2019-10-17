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
A script to fix the 'from . import resources_icons_rc' statement in the files generated by pyside-uic

:authors: A. Soininen (VTT)
:date:   30.9.2019
"""


if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]
    lines = list()
    with open(file_name, 'r') as in_file:
        for line in in_file:
            if line == "from . import resources_icons_rc\n":
                lines.append("from spinetoolbox import resources_icons_rc\n")
            elif line == "from . import resources_logos_rc\n":
                lines.append("from spinetoolbox import resources_logos_rc\n")
            else:
                lines.append(line)
    with open(file_name, 'w') as out_file:
        out_file.writelines(lines)