"""
Contains settings classes
1. Standard settings(_StandardSettings)
2. Settings while the application is running(RuntimeSettings)

version: 1.0.1 - valid version

versions-list:  0.0.1 - create class _StandardSettings
                0.0.2 - create class RuntimeSettings
                0.0.3 - description of the _StandardSettings class
                0.0.4 - description of the RuntimeSettings class
                0.0.5 - enabling downloading local settings from files for the RuntimeSettings class
                1.0.0 - first release version, can load images, resources files, stylesheet-files
                1.0.1 - first release version, can load sql-scripts files


author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import argparse
import os.path
import random
import sys
import json
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, QColor


class _StandardSettings:

    def __init__(self):
        self.__DEBUG__ = True
        self.__CHARSET__ = 'UTF-8'

        # Directory workspace
        self._ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
        self._RESOURCES_DIR = os.path.join(self._ROOT_DIR, '.resources')
        self._IMAGE_DIR = os.path.join(self._RESOURCES_DIR, 'images')
        self._STYLESHEETS_DIR = os.path.join(self._RESOURCES_DIR, 'styles')
        self._SQL_SCRIPTS_DIR = os.path.join(self._RESOURCES_DIR, 'sql-scripts')
        self._check_dirs()

        self._STYLESHEETS_DICT = dict()
        self._load_stylesheets_dict()

        self.TITLE = 'StudentAccounting'
        self.VERSION = '0.0.1'
        self.STYLESHEET = None
        if len(self._STYLESHEETS_DICT.keys()) > 0:
            self.STYLESHEET = random.choice(self._STYLESHEETS_DICT.keys())

    def debug(self) -> bool:
        return self.__DEBUG__

    def charset(self) -> str:
        return self.__CHARSET__

    def get_resource_filepath(self, filename: str) -> str | os.PathLike:
        if filename is None:
            raise FileNotFoundError("Empty filename for resources files is invalid")

        return os.path.join(self._RESOURCES_DIR, str(filename))

    def get_resources_filedata(self, filename: str) -> str:
        filepath = self.get_resource_filepath(filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'File {filepath} not found at resources directory')

        filedata = ''
        with open(filepath, 'r', encoding=self.charset()) as file:
            filedata = file.read()

        return filedata

    def get_image_filepath(self, image_filename: str) -> str | os.PathLike:
        if image_filename is None:
            raise FileNotFoundError("Empty filename for resources files is invalid")

        return os.path.join(self._IMAGE_DIR, image_filename)

    def load_image(self, image_filename: str) -> QIcon:
        icon = QIcon()
        icon.addPixmap(self.load_pixmap(image_filename))
        return icon

    def load_pixmap(self, pixmap_filename: str, default_size=QSize(50, 50), default_color=QColor(0, 0, 0, 255)):
        pixmap_filepath = self.get_image_filepath(pixmap_filename)
        if not os.path.join(pixmap_filepath):
            pixmap = QPixmap(default_size)
            pixmap.fill(default_color)
            return pixmap

        return QPixmap(pixmap_filepath)

    def get_stylesheet_filepath(self, filename: str) -> os.PathLike | str:
        if filename is None:
            raise FileNotFoundError("Empty filename for stylesheet files is invalid")

        return os.path.join(self._STYLESHEETS_DIR, str(filename))

    def _get_stylesheet_filedata(self, filename: str) -> str:
        filepath = self.get_stylesheet_filepath(filename)
        if not os.path.exists(filepath):
            return ''

        data = ''
        with open(filepath, 'r', encoding=self.charset()) as stylesheet_file:
            data = stylesheet_file.read()

        return data

    def get_stylesheet(self, stylesheet_name: str) -> str:
        if not self.is_have_stylesheet(stylesheet_name):
            raise AttributeError(f'Stylesheet ID-name {stylesheet_name} is not found it is invalid')

        return self._get_stylesheet_filedata(self._STYLESHEETS_DICT[stylesheet_name])

    def is_have_stylesheet(self, stylesheet: str) -> bool:
        return stylesheet in self._STYLESHEETS_DICT.keys()

    def _load_stylesheets_dict(self):
        for child in os.listdir(self._STYLESHEETS_DIR):
            child_path = os.path.join(self._STYLESHEETS_DIR, child)
            if os.path.isfile(child_path) and child_path.endswith('.css') and len(child.replace('.css', '')) > 0:
                name = child.strip('.').lower().replace('_', '-')
                name = ' '.join(name.split('.')[:-1])
                name = '-'.join(name.strip().split())
                self._STYLESHEETS_DICT[name] = child

    def get_stylesheet_names(self) -> set[str]:
        return self._STYLESHEETS_DICT.keys()

    def _check_dirs(self):
        for item in dir(self):
            if item.startswith('_') and item.isupper() and item.endswith('_DIR'):
                dir_path = self.__getattribute__(item)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

    def get_sql_script_filepath(self, script_name: str):
        return os.path.join(self._SQL_SCRIPTS_DIR, script_name)

    def get_sql_script_filedata(self, script_name: str):
        script_path = self.get_sql_script_filepath(script_name)
        if not os.path.exists(script_path) or not os.path.isfile(script_path):
            return ''

        data = ''
        with open(script_path, 'r', encoding=self.charset()) as script_file:
            data = script_file.read()

        return data


class RuntimeSettings(_StandardSettings):

    def __init__(self, *args):
        super().__init__()
        if len(args) == 0:
            args = tuple(sys.argv[1:])
        self._load_from_local_settings_file()  # last runtime settings
        self._initialize_by_system_args(self._parse_system_args(*args))  # new runtime settings

    def _parse_system_args(self, *args) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            prog=self.TITLE,
            description='-'
        )
        parser.add_argument(
            '-d', '--debug',
            default=self.debug(),
            action=f'store_{str(not self.debug()).lower()}',
            help=f'Set debug mode as {not self.debug()}'
        )
        parser.add_argument(
            '-t', '--title',
            default=self.TITLE, type=str,
            help='Change application title'
        )
        parser.add_argument(
            '-sv', '--set-version',
            default=self.VERSION,
            type=str,
            help='Change application version at format \'<release>.<bugfix>.<beta>\''
        )
        parser.add_argument(
            '-v', '--version',
            action='version',
            version=f'{self.TITLE} version: {self.VERSION}',
            help='Print version information of application'
        ),
        parser.add_argument(
            '-css', '--style-sheet',
            default=self.STYLESHEET,
            type=str,
            help='Change application runtime stylesheet'
        )
        return parser.parse_args(args)

    def _initialize_by_system_args(self, ns: argparse.Namespace):
        self.__DEBUG__ = bool(ns.debug)
        self.TITLE = str(ns.title)
        self.VERSION = self._check_version(ns.set_version)
        self.STYLESHEET = self._check_stylesheet(ns.style_sheet)

    def _load_from_local_settings_file(self):
        settings_filepath = self.get_resource_filepath('settings.json')
        if not os.path.exists(settings_filepath):
            self._save_to_local_settings_file()
            return

        data = {}
        try:
            with open(settings_filepath, 'r', encoding=self.charset()) as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError as _:
            data = {}

        if not isinstance(data, dict) or len(data.keys()) == 0:
            self._save_to_local_settings_file()
            return

        for data_item in data.keys():
            attr = str(data_item).upper()
            if hasattr(self, attr) and data[data_item] is not None:
                self.__setattr__(attr, data[data_item])

    def _save_to_local_settings_file(self):
        settings_filepath = self.get_resource_filepath('settings.json')
        data = self._to_json_object()
        with open(settings_filepath, 'w', encoding=self.charset()) as file:
            json.dump(data, file, indent=2)

    def close(self):
        self._save_to_local_settings_file()

    def _check_version(self, version: str):
        v_data = version.split('.')
        if len(v_data) != 3:
            return self.VERSION

        for p in v_data:
            if not p.isdigit():
                return self.VERSION

        if self.VERSION < version:
            return version

        return self.VERSION

    def _check_stylesheet(self, style_sheet: str):
        if style_sheet is None:
            return self.STYLESHEET

        if self.is_have_stylesheet(style_sheet):
            return style_sheet

        print(f'Stylesheet ID-name {style_sheet} is not found it is invalid')
        return self.STYLESHEET

    def _to_json_object(self):
        json_object = {}
        items = []
        for item in dir(self):
            if item.isupper() and not item.startswith('_'):
                items.append(item)

        items.sort()
        items.reverse()

        for item in items:
            json_object[item.lower()] = self.__getattribute__(item)

        return json_object


if __name__ == '__main__':
    settings = RuntimeSettings()
    settings.close()
