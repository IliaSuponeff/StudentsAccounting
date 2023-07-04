"""
Contains class which exercises control over views.windows.ui_main_window.Ui_MainWindow

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import math

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
        self._load_students_info()

    def setHandlers(self):
        self._ui.student_choose_box.currentIndexChanged.connect(self._move_to_student)
        self._ui.next_student_btn.clicked.connect(self._next_student)
        self._ui.prev_student_btn.clicked.connect(self._prev_student)
        self._ui.del_student_btn.clicked.connect(self._delete_student)
        self._ui.add_student_btn.clicked.connect(self._add_student)

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
        self._ui.next_student_btn.setIcon(
            self.settings.load_image('next_student.png')
        )
        self._ui.prev_student_btn.setIcon(
            self.settings.load_image('prev_student.png')
        )
        self._ui.del_student_btn.setIcon(
            self.settings.load_image('remove_student.png')
        )
        self._ui.del_visit_btn.setIcon(
            self.settings.load_image('remove_visit.png')
        )

    def load_current_student(self):
        student = self.get_current_student()

        self._ui.student_name_lbl.setText('-' if student is None else student.name())
        self._ui.student_summary_result_lbl.setText(
            '' if student is None else str(self.get_student_summary_result(student))
        )
        self._ui.student_currency_lbl.setText('' if student is None else student.currency().value)
        self._ui.student_choose_box.setCurrentIndex(self._current_student_index)

    def get_current_student(self):
        if 0 <= self._current_student_index < len(self.students):
            return self.students[self._current_student_index]

        return None

    def get_student_summary_result(self, student: Student) -> int:
        summary_result = 0
        return 0
        student_visits: list[Visit] = self.database.get_student_visits(student)
        for visit in student_visits:
            if bool(visit.is_special()):
                summary_result += abs(visit.special_sum())
            else:
                summary_result += visit.timespan() * student.hour_cost()

        return summary_result

    def _next_student(self):
        if len(self.students) == 0:
            return

        self._move_to_student((self._current_student_index + 1) % len(self.students))

    def _prev_student(self):
        if len(self.students) == 0:
            return

        self._move_to_student((self._current_student_index - 1) % len(self.students))

    def _move_to_student(self, index):
        if not (0 <= index < len(self.students)):
            # unchanged current student index
            return

        self._current_student_index = index
        self.load_current_student()

    def _delete_student(self):
        student = self.get_current_student()
        if student is None:
            return

        self.database.remove_student(student)
        self._load_students_info()
        while not (0 <= self._current_student_index < len(self.students)):
            self._prev_student()

    def _load_students_info(self):
        self.students = self.database.students
        self._ui.student_choose_box.clear()
        self._ui.student_choose_box.addItems(
            [student.name() for student in self.students]
        )
        self.load_current_student()

    def _add_student(self):
        pass
