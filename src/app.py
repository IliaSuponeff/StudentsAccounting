"""
Contains class  which run mainloop of app and close all components

version: 0.0.3

versions-list:  0.0.1 - create simple Application class template
                0.0.2 - connect to Application class template settings class
                0.0.3 - connect to Application class template database class


author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import sys
from settings import RuntimeSettings
from PySide6.QtWidgets import QApplication
from controllers.database import DataBase
from controllers.main_window import MainWindowHandler


class Application(QApplication):

    def __init__(self):
        super().__init__()
        self.settings = RuntimeSettings(*sys.argv[1:])
        self.db = DataBase(self.settings)
        self.main_window = MainWindowHandler(self.settings, self.db)

    def exec(self) -> int:
        self.run()
        exit_code = super().exec()
        self.settings.close()
        self.db.close()
        return exit_code

    def run(self):
        self.main_window.show()


if __name__ == '__main__':
    app = Application()
    sys.exit(app.exec())
