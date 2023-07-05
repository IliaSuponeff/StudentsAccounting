"""
Contains class which exercises control over views.dialogs.ui_create_visit.Ui_CreatorVisit

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from views.dialogs.ui_create_visit import Ui_CreatorVisit
from settings import RuntimeSettings
from controllers.database import DataBase, Student, Visit, Currency
from controllers.user_exception_mgs_dialogs import exception, warning


class AddStudentVisitDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, database: DataBase, student: Student):
        super().__init__()
        assert student is not None, "Not have chosen student to add him visit"
        self.settings = settings
        self.db = database
        self._student = student
        self._ui = Ui_CreatorVisit()
        self.setUi()
        self.setHandlers()

    def setUi(self):
        self._ui.setupUi(self)
        self.setWindowTitle(f'Add visit for {self._student.name()} student')
        self._ui.dialog_title_lbl.setText(self.windowTitle())
        date_now = datetime.date.today()
        self._ui.choose_date_edit.setDate(
            QDate(date_now.year, date_now.month, date_now.day)
        )
        self._ui.currency_lbl.setText(self._student.currency().value)

    def setHandlers(self):
        self._ui.done_btn.clicked.connect(lambda: self.add_visit())

    def add_visit(self):
        date = self._ui.choose_date_edit.date()
        date = datetime.datetime.strptime(
            f'{date.day()}.{date.month()}.{date.year()}',
            '%d.%m.%Y'
        ).date()
        timespan = self._ui.timespan_spinbox.value()
        is_special = self._ui.special_rbtn.isChecked()
        special_sum = self._ui.sp_sum_spinbox.value() if is_special else 0
        try:
            visit = Visit(date, timespan, is_special, special_sum)
            print(visit)
            self.db.add_student_visit(self._student, visit)
            del visit
            self.close()
        except Exception as ex:
            exception(
                icon=self.windowIcon(),
                msg='\n'.join([str(arg) for arg in ex.args]).strip()
            )
