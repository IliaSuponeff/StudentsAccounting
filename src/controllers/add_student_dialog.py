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


class AddStudentDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.db = database
        self._CREATE_STUDENT = False
        self._ui = Ui_CreaterStudent()
        self._ui.setupUi(self)

    def call(self, *args):
        self.setUi()
        self.setHandlers()
        self._CREATE_STUDENT = False

    def setUi(self):
        self.setWindowTitle('Add student')
        self._ui.dialog_title_lbl.setText(self.windowTitle())
        self._ui.done_btn.setText('Add')
        self._ui.name_le.setText('')
        self._ui.hour_cost_spin_box.setValue(1.0)
        self._ui.currency_box.clear()
        self._ui.currency_box.addItems([str(currency) for currency in Currency.all()])

    def setHandlers(self):
        self._ui.done_btn.clicked.connect(self._create_student)

    def _create_student(self):
        if self._CREATE_STUDENT:
            return

        name = self._ui.name_le.text()
        hour_cost = self._ui.hour_cost_spin_box.value()
        currency = self._ui.currency_box.currentText()
        try:
            student: Student = Student.create_new_student(name, hour_cost, currency)
            if student in self.db.students:
                raise AssertionError(f"Student {student.name()} is exists now")

            self.db.add_student(student)
            self.close()
            self._CREATE_STUDENT = True
        except AssertionError as ex:
            exception(
                icon=self.windowIcon(),
                msg='\n'.join(ex.args).strip()
            )
