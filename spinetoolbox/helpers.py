######################################################################################################################
# Copyright (C) 2017 - 2018 Spine project consortium
# This file is part of Spine Toolbox.
# Spine Toolbox is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option)
# any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General
# Public License for more details. You should have received a copy of the GNU Lesser General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
######################################################################################################################

"""
General helper functions and classes.

:authors: P. Savolainen (VTT)
:date:   10.1.2018
"""

import sys
import logging
import datetime
import os
import time
import shutil
import glob
import json
import spinedb_api
from PySide2.QtCore import Qt, Slot
from PySide2.QtCore import __version__ as qt_version
from PySide2.QtCore import __version_info__ as qt_version_info
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtGui import QCursor, QImageReader
from config import DEFAULT_PROJECT_DIR, REQUIRED_SPINEDB_API_VERSION


def set_taskbar_icon():
    """Set application icon to Windows taskbar."""
    if os.name == "nt":
        import ctypes
        myappid = "{6E794A8A-E508-47C4-9319-1113852224D3}"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


@Slot(name="supported_img_formats")
def supported_img_formats():
    """Function to check if reading .ico files is supported."""
    img_formats = QImageReader().supportedImageFormats()
    img_formats_str = '\n'.join(str(x) for x in img_formats)
    logging.debug("Supported Image formats:\n{0}".format(img_formats_str))


def pyside2_version_check():
    """Check that PySide2 version is older than 5.12, since this is not supported yet.
    Issue #238 in GitLab.

    qt_version is the Qt version used to compile PySide2 as string. E.g. "5.11.2"
    qt_version_info is a tuple with each version component of Qt used to compile PySide2. E.g. (5, 11, 2)
    """
    # print("Your QT version info is:{0} version string:{1}".format(qt_version_info, qt_version))
    if qt_version_info[0] == 5 and qt_version_info[1] >= 12:
        print(
            """Sorry for the inconvenience but,

            Spine Toolbox does not support PySide2 version {0} yet.
            Please downgrade PySide2 to version 5.11.x and try to start the application again.

            To downgrade PySide2 to a compatible version, run

                pip install "pyside2<5.12"

            """.format(qt_version))
        return False
    return True


def spinedb_api_version_check():
    """Check if spinedb_api is the correct version and explain how to upgrade if it is not."""
    try:
        current_version = spinedb_api.__version__
        current_split = [int(x) for x in current_version.split(".")]
        required_split = [int(x) for x in REQUIRED_SPINEDB_API_VERSION.split(".")]
        if current_split >= required_split:
            return True
    except AttributeError:
        current_version = "not reported"
    script = "upgrade_spinedb_api.bat" if sys.platform == "win32" else "upgrade_spinedb_api.sh"
    print(
        """ERROR:
        Spine Toolbox failed to start because spinedb_api is outdated.
        (Required version is {0}, whereas current is {1})
        Please upgrade spinedb_api to v{0} and start Spine Toolbox again.

        To upgrade, run script '{2}' in the '/bin' folder.

        Or upgrade it manually by running,

            pip install --upgrade git+https://github.com/Spine-project/Spine-Database-API.git

        """.format(REQUIRED_SPINEDB_API_VERSION, current_version, script))
    return False


def busy_effect(func):
    """ Decorator to change the mouse cursor to 'busy' while a function is processed.

    Args:
        func: Decorated function.
    """
    def new_function(*args, **kwargs):
        # noinspection PyTypeChecker, PyArgumentList, PyCallByClass
        QApplication.setOverrideCursor(QCursor(Qt.BusyCursor))
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception("Error {}".format(e.args[0]))
            raise e
        finally:
            # noinspection PyArgumentList
            QApplication.restoreOverrideCursor()
    return new_function


def project_dir(qsettings):
    """Returns current project directory.

    Args:
        qsettings (QSettings): Settings object
    """
    # NOTE: This is not actually used. The key is not saved to qsettings anywhere. This is a placeholder for code
    # if we want to be able to change the projects directory at some point.
    proj_dir = qsettings.value("appSettings/projectsDir", defaultValue="")
    if not proj_dir:
        return DEFAULT_PROJECT_DIR
    else:
        return proj_dir


def get_datetime(show):
    """Returns date and time string for appending into Event Log messages.

    Args:
        show (boolean): True returns date and time string. False returns empty string.
    """
    if show:
        t = datetime.datetime.now()
        return "[{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}] ".format(t.day, t.month, t.year, t.hour, t.minute, t.second)
    else:
        return ""


def create_dir(base_path, folder='', verbosity=False):
    """Create (input/output) directories recursively.

    Args:
        base_path (str): Absolute path to wanted dir
        folder (str): (Optional) Folder name. Usually short name of item.
        verbosity (bool): True prints a message that tells if the directory already existed or if it was created.

    Returns:
        True if directory already exists or if it was created successfully.

    Raises:
        OSError if operation failed.
    """
    directory = os.path.join(base_path, folder)
    if os.path.exists(directory):
        if verbosity:
            logging.debug("Directory found: {0}".format(directory))
        return True
    else:
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError:
            raise
        if verbosity:
            logging.debug("Directory created: {0}".format(directory))
        return True


def create_output_dir_timestamp():
    """ Creates a new timestamp string that is used as Tool output
    directory.

    Returns:
        Timestamp string or empty string if failed.
    """
    try:
        # Create timestamp
        stamp = datetime.datetime.fromtimestamp(time.time())
    except OverflowError:
        logging.error('Timestamp out of range.')
        return ''
    extension = stamp.strftime('%Y-%m-%dT%H.%M.%S')
    return extension


@busy_effect
def copy_files(src_dir, dst_dir, includes=None, excludes=None):
    """Method for copying files. Does not copy folders.

    Args:
        src_dir (str): Source directory
        dst_dir (str): Destination directory
        includes (list): Included files (wildcards accepted)
        excludes (list): Excluded files (wildcards accepted)

    Returns:
        count (int): Number of files copied
    """
    if not includes:
        includes = ['*']
    if not excludes:
        excludes = []
    src_files = []
    for pattern in includes:
        src_files += glob.glob(os.path.join(src_dir, pattern))
    exclude_files = []
    for pattern in excludes:
        exclude_files += glob.glob(os.path.join(src_dir, pattern))
    count = 0
    for filename in src_files:
        if os.path.isdir(filename):
            continue
        if filename not in exclude_files:
            shutil.copy(filename, dst_dir)
            count += 1
    return count


@busy_effect
def erase_dir(path, verbosity=False):
    """Delete directory and all its contents without prompt.

    Args:
        path (str): Path to directory
        verbosity (bool): Print logging messages or not
    """
    if not os.path.exists(path):
        if verbosity:
            logging.debug("Path does not exist: {}".format(path))
        return False
    if verbosity:
        logging.debug("Deleting directory {0}".format(path))
    try:
        shutil.rmtree(path)
    except OSError:
        raise
    return True


@busy_effect
def copy_dir(widget, src_dir, dst_dir):
    """Make a copy of a directory. All files and folders are copied.

    Args:
        widget (QWidget): Parent widget for QMessageBoxes
        src_dir (str): Absolute path to directory that will be copied
        dst_dir (str): Absolute path to new directory
    """
    title_msg = "Copying directory failed"
    try:
        shutil.copytree(src_dir, dst_dir)
    except FileExistsError:
        msg = "Directory<br/><b>{0}</b><br/>already exists".format(dst_dir)
        # noinspection PyTypeChecker, PyArgumentList, PyCallByClass
        QMessageBox.information(widget, title_msg, msg)
        return False
    except PermissionError as e:
        logging.exception(e)
        msg = "Access to directory <br/><b>{0}</b><br/>denied." \
              "<br/><br/>Possible reasons:" \
              "<br/>1. Windows Explorer is open in the directory" \
              "<br/>2. Permission error" \
              "<br/><br/>Check these and try again.".format(dst_dir)
        # noinspection PyTypeChecker, PyArgumentList, PyCallByClass
        QMessageBox.information(widget, title_msg, msg)
        return False
    except OSError:
        msg = "Copying directory failed. OSError in" \
              "<br/><b>{0}</b><br/>Possibly because Windows " \
              "Explorer is open in the directory".format(dst_dir)
        # noinspection PyTypeChecker, PyArgumentList, PyCallByClass
        QMessageBox.information(widget, title_msg, msg)
        return False
    return True


def rename_dir(widget, old_dir, new_dir):
    """Rename directory. Note: This is not used in renaming projects due to unreliability.
    Looks like it works fine in renaming project items though.

    Args:
        widget (QWidget): Parent widget for QMessageBoxes
        old_dir (str): Absolute path to directory that will be renamed
        new_dir (str): Absolute path to new directory
    """
    try:
        shutil.move(old_dir, new_dir)
    except FileExistsError:
        msg = "Directory<br/><b>{0}</b><br/>already exists".format(new_dir)
        # noinspection PyTypeChecker, PyArgumentList, PyCallByClass
        QMessageBox.information(widget, "Renaming directory failed", msg)
        return False
    except PermissionError as e:
        logging.exception(e)
        msg = "Access to directory <br/><b>{0}</b><br/>denied." \
              "<br/><br/>Possible reasons:" \
              "<br/>1. Windows Explorer is open in the directory" \
              "<br/>2. Permission error" \
              "<br/><br/>Check these and try again.".format(old_dir)
        # noinspection PyTypeChecker, PyArgumentList, PyCallByClass
        QMessageBox.information(widget, "Renaming directory failed", msg)
        return False
    except OSError:
        msg = "Renaming input directory failed. OSError in" \
              "<br/><b>{0}</b><br/>Possibly because Windows " \
              "Explorer is open in the directory".format(old_dir)
        # noinspection PyTypeChecker, PyArgumentList, PyCallByClass
        QMessageBox.information(widget, "Renaming directory failed", msg)
        return False
    return True


def fix_name_ambiguity(name_list, offset=0):
    """Modify repeated entries in name list by appending an increasing integer."""
    ref_name_list = name_list.copy()
    ocurrences = {}
    for i, name in enumerate(name_list):
        n_ocurrences = ref_name_list.count(name)
        if n_ocurrences == 1:
            continue
        ocurrence = ocurrences.setdefault(name, 1)
        name_list[i] = name + str(offset + ocurrence)
        ocurrences[name] = ocurrence + 1


def tuple_itemgetter(itemgetter_func, num_indexes):
    """Change output of itemgetter to always be a tuple even for one index"""
    if num_indexes == 1:
        def g(item):
            return (itemgetter_func(item),)
        return g
    else:
        return itemgetter_func


def format_string_list(str_list):
    """
    Return an unordered html list with all elements in str_list.
    Intended to print error logs as returned by spinedb_api.

    Args:
        str_list (list(str))
    """
    return "<ul>" + "".join(["<li>" + str(x) + "</li>" for x in str_list]) + "</ul>"


def strip_json_data(data, maxlen):
    """Return a json equivalent to data, stripped to maxlen characters.
    """
    if not data:
        return data
    try:
        stripped_data = json.dumps(json.loads(data))
    except json.JSONDecodeError:
        stripped_data = data
    if len(stripped_data) > 2 * maxlen:
        stripped_data = stripped_data[:maxlen] + "..." + stripped_data[-maxlen:]
    return stripped_data
