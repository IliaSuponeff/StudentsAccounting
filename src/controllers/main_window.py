"""
Contains class which exercises control over views.windows.ui_main_window.Ui_MainWindow

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""

from PySide6.QtWidgets import QMainWindow, QHeaderView
from views.windows.ui_main_window import Ui_MainWindow
from controllers.database import DataBase, Student, Visit, Currency
from settings import RuntimeSettings


class MainWindowHandler(QMainWindow):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.database = database
        self.students = self.database.students
        self._current_student_index = 0
        self._ui = Ui_MainWindow()
        self.setUi()
        self.setHandlers()

    def setUi(self):
        self._ui.setupUi(self)
        self.setIcons()
        self._ui.student_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._ui.active_student_choose_box.addItems()

    def setHandlers(self):
        pass

    def setIcons(self):
        self._ui.add_student_btn.setIcon(
            self.settings.load_image('add_student.png')
        )
        self._ui.add_visit_btn.setIcon(
            self.settings.load_image('add_visit.png')
        )
        self._ui.edit_student_btn.setIcon(
            self.settings.load_image('edit.png')
        )
        self._ui.edit_visit_btn.setIcon(
            self.settings.load_image('edit.png')
        )
        self._ui.next_active_student_btn.setIcon(
            self.settings.load_image('next_student.png')
        )
        self._ui.prev_active_student_btn.setIcon(
            self.settings.load_image('prev_student.png')
        )
        self._ui.del_student_btn.setIcon(
            self.settings.load_image('remove_student.png')
        )
        self._ui.del_visit_btn.setIcon(
            self.settings.load_image('remove_visit.png')
        )

