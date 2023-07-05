"""
Contains class which exercises control over views.windows.ui_main_window.Ui_MainWindow

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import math
import pprint

from PySide6.QtWidgets import QMainWindow, QHeaderView, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from views.windows.ui_main_window import Ui_MainWindow
from controllers.database import DataBase, Student, Visit, Currency
from settings import RuntimeSettings
from controllers.add_student_dialog import AddStudentDialog


class MainWindowHandler(QMainWindow):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.database = database
        self.students = self.database.students
        self._current_student_index = 0
        self._table_modal = QStandardItemModel()
        self._ui = Ui_MainWindow()
        self.setUi()
        self.setHandlers()

    def setUi(self):
        self._ui.setupUi(self)
        self.setIcons()
        self._ui.student_visits_table_view.setModel(self.build_table_modal())
        self._ui.student_visits_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._load_students_info()

    def setHandlers(self):
        self._ui.student_choose_box.currentIndexChanged.connect(self._move_to_student)
        self._ui.next_student_btn.clicked.connect(self._next_student)
        self._ui.prev_student_btn.clicked.connect(self._prev_student)
        self._ui.del_student_btn.clicked.connect(self._delete_student)
        self._ui.add_student_btn.clicked.connect(lambda: self._call_dialog(AddStudentDialog))
        self._ui.del_visit_btn.clicked.connect(self._delete_visit)

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

        self._load_current_student_visits()

    def get_current_student(self):
        if 0 <= self._current_student_index < len(self.students):
            return self.students[self._current_student_index]

        return None

    def get_student_summary_result(self, student: Student) -> int:
        if student is None:
            return 0

        student_visits: list[Visit] = self.database.get_student_visits(student)
        summary_result = 0
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
        while not (0 <= self._current_student_index < len(self.students)) and len(self.students) > 0:
            self._prev_student()

    def _load_students_info(self):
        self.students = self.database.students
        self._ui.student_choose_box.clear()
        self._ui.student_choose_box.addItems(
            [student.name() for student in self.students]
        )
        self.load_current_student()

    def _call_dialog(self, _dialog_class_link, *args):
        dialog: QDialog = _dialog_class_link(self.settings, self.database, *args)
        dialog.show()
        dialog.exec()
        self._load_students_info()
        del dialog

    def _load_current_student_visits(self):
        student = self.get_current_student()
        if student is None:
            # len(self.students) == 0
            return
        visits: list[Visit] = self.database.get_student_visits(student)
        if self.settings.debug():
            pprint.pprint(visits)

        self._table_modal.clear()
        self.build_table_modal()

        for visit in visits:
            self._table_modal.appendRow(
                [
                    QStandardItem(str(visit.date())),
                    QStandardItem(str(visit.timespan())),
                    QStandardItem(
                        str(
                            visit.special_sum() if visit.is_special() else visit.timespan() * student.hour_cost()
                        )
                    )
                ]

            )

    def build_table_modal(self):
        self._table_modal.setHorizontalHeaderLabels(
            ['Date', 'Timespan', 'Summary']
        )
        return self._table_modal

    def _delete_visit(self):
        indexes = self._ui.student_visits_table_view.selectedIndexes()
        print(indexes)
