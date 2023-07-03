"""
Contains class which exercises control over views.windows.ui_main_window.Ui_MainWindow

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""

from PySide6.QtWidgets import QMainWindow
from views.windows.ui_main_window import Ui_MainWindow
from controllers.database import DataBase
from settings import RuntimeSettings


class MainWindowHandler(QMainWindow):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.database = database
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
