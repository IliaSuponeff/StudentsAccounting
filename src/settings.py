"""
Contains settings classes
1. Standard settings(_StandardSettings)
2. Settings while the application is running(RuntimeSettings)

version: 0.0.2

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import argparse
import sys


class _StandardSettings:

    def __init__(self):
        pass


class RuntimeSettings(_StandardSettings):

    def __init__(self):
        super().__init__()
        self._initialize_by_system_args(self._parse_system_args(*sys.argv[1:]))
        self._load_from_local_settings_file()

    def _parse_system_args(self, *args):
        pass

    def _initialize_by_system_args(self, ns: argparse.Namespace):
        pass

    def _to_xml_object(self):
        pass

    def _load_from_local_settings_file(self):
        pass

    def _save_to_local_settings_file(self):
        pass

    def close(self):
        pass
