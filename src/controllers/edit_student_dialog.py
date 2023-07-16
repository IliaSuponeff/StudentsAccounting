"""
Contains class which exercises control over views.dialogs.ui_create_student.Ui_CreaterStudent

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from PySide6.QtWidgets import QDialog
from views.dialogs.ui_create_student import Ui_CreaterStudent
from settings import RuntimeSettings
from controllers.database import DataBase, Student, Currency
from controllers.user_exception_mgs_dialogs import exception


class EditStudentDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.db = database
        self._old_student: Student = None
        self._ui = Ui_CreaterStudent()
        self._ui.setupUi(self)
        self.setHandlers()

    def call(self, student: Student, *args):
        assert student is not None, "Not have chosen student to edit him."
        self._old_student = student
        self.setUi()

    def setUi(self):
        self.setWindowTitle(f'Edit student {self._old_student.name()}')
        self._ui.dialog_title_lbl.setText(self.windowTitle())
        self._ui.done_btn.setText('Edit')
        self._ui.name_le.setText(f'{self._old_student.name()}')
        self._ui.hour_cost_spin_box.setValue(self._old_student.hour_cost())
        self._ui.currency_box.clear()
        self._ui.currency_box.addItems([str(currency) for currency in Currency.all()])
        self._ui.currency_box.setCurrentText(self._old_student.currency().value)
        self.setStyleSheet(self.settings.get_stylesheet(self.settings.STYLESHEET))

    def setHandlers(self):
        self._ui.done_btn.clicked.connect(self._edit_student)

    def _edit_student(self):
        name = self._ui.name_le.text()
        hour_cost = self._ui.hour_cost_spin_box.value()
        currency = self._ui.currency_box.currentText()
        try:
            student: Student = Student.create_new_student(name, hour_cost, currency)
            if student == self._old_student:
                self.close()

            if student in self.db.students:  # and student != self._old_student
                raise AssertionError(f"Student {student.name()} is exists now")

            self.db.edit_student(self._old_student, student)
            self.close()
        except AssertionError as ex:
            exception(
                icon=self.windowIcon(),
                msg='\n'.join(ex.args).strip()
            )