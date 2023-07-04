"""
Contains class which exercises control over views.dialogs.ui_create_student.Ui_CreaterStudent

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from PySide6.QtWidgets import QDialog
from views.dialogs.ui_create_student import Ui_CreaterStudent
from settings import RuntimeSettings
from controllers.database import DataBase, Student, Visit, Currency
from controllers.user_exception_mgs_dialogs import exception


class AddStudentDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.db = database
        self._ui = Ui_CreaterStudent()
        self.setUi()
        self.setHandlers()

    def setUi(self):
        self._ui.setupUi(self)
        self.setWindowTitle('Add student')
        self._ui.dialog_title_lbl.setText(self.windowTitle())
        self._ui.done_btn.setText('Add')

    def setHandlers(self):
        self._ui.done_btn.clicked.connect(lambda: self._create_student())
        self._ui.currency_box.addItems([str(currency) for currency in Currency.all()])

    def _create_student(self):
        name = self._ui.name_le.text()
        hour_cost = self._ui.hour_cost_spin_box.value()
        currency = self._ui.currency_box.currentText()
        try:
            student: Student = Student.create_new_student(name, hour_cost, currency)
            self.db.add_student(student)
        except Exception as ex:
            exception(
                icon=self.windowIcon(),
                msg='\n'.join(ex.args).strip()
            )
