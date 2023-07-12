"""
Contains class which exercises control over views.dialogs.ui_create_visit.Ui_CreatorVisit

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime

import PySide6.QtGui
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from views.dialogs.ui_create_visit import Ui_CreatorVisit
from settings import RuntimeSettings
from controllers.database import DataBase, Student, Visit, Currency
from controllers.user_exception_mgs_dialogs import exception, warning


class AddStudentVisitDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.db = database
        self._student = None
        self._IS_ADD_VISIT = False
        self._ui = Ui_CreatorVisit()
        self._ui.setupUi(self)

    def setUi(self):
        self.setWindowTitle(f'Add visit for {self._student.name()} student')
        self._ui.dialog_title_lbl.setText(self.windowTitle())
        date_now = datetime.date.today()
        self._ui.visit_date_edit.setDate(
            QDate(date_now.year, date_now.month, date_now.day)
        )
        self._ui.timespan_spinbox.setValue(1.0)
        self._ui.currency_lbl.setText(self._student.currency().value)
        self._ui.unspecial_rbtn.setChecked(True)
        self._ui.special_sum_frame.hide()
        self._ui.sp_sum_spinbox.setValue(0.0)

    def setHandlers(self):
        self._ui.unspecial_rbtn.clicked.connect(lambda: self._ui.special_sum_frame.hide())
        self._ui.special_rbtn.clicked.connect(lambda: self._ui.special_sum_frame.show())
        self._ui.done_btn.clicked.connect(lambda: self.add_visit())

    def call(self, student, *args):
        assert student is not None, "Not have chosen student to add him visit"
        self._student = student
        self._IS_ADD_VISIT = False
        self.setUi()
        self.setHandlers()

    def add_visit(self):
        if self._IS_ADD_VISIT:
            return

        date = self._ui.visit_date_edit.date()
        date = datetime.datetime.strptime(
            f'{date.day()}.{date.month()}.{date.year()}', '%d.%m.%Y'
        ).date()
        timespan = self._ui.timespan_spinbox.value()
        is_special = self._ui.special_rbtn.isChecked()
        special_sum = self._ui.sp_sum_spinbox.value() if is_special else 0
        try:
            visit = Visit(date, timespan, is_special, special_sum)
            if visit in self.db.get_student_visits(self._student):

                raise AssertionError(
                    f"Visit {visit.date().strftime('%d.%m.%Y')} with timespan {visit.timespan()}"
                    f"{f' and sum={visit.special_sum()}' if visit.is_special() else ''} is exists now."
                )

            self.db.add_student_visit(self._student, visit)
            self.close()
            self._IS_ADD_VISIT = True
            return
        except Exception as ex:
            exception(
                icon=self.windowIcon(),
                msg='\n'.join([str(arg) for arg in ex.args]).strip()
            )
            self._IS_ADD_VISIT = False
