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
        self._ui = Ui_CreaterStudent()
        self._ui.setupUi(self)
        self.setHandlers()

    def call(self, *args):
        self.setUi()

    def setUi(self):
        self.setWindowTitle('Добавление студента')
        self._ui.dialog_title_lbl.setText(self.windowTitle())
        self._ui.done_btn.setText('Добавить')
        self._ui.name_le.setText('')
        self._ui.hour_cost_spin_box.setValue(1.0)
        self._ui.currency_box.clear()
        self._ui.currency_box.addItems([str(currency) for currency in Currency.all()])
        self.setStyleSheet(self.settings.get_stylesheet(self.settings.STYLESHEET))

    def setHandlers(self):
        self._ui.done_btn.clicked.connect(lambda: self._create_student())

    def _create_student(self):
        name = self._ui.name_le.text()
        hour_cost = self._ui.hour_cost_spin_box.value()
        currency = self._ui.currency_box.currentText()
        try:
            student: Student = Student.create_new_student(name, hour_cost, currency)

            if student.name() in [_student.name() for _student in self.db.students]:
                raise AssertionError(f"Студент {student.name()} уже существует")

            self.db.add_student(student)
            self.close()
        except AssertionError as ex:
            exception(
                icon=self.windowIcon(),
                msg='\n'.join(ex.args).strip(),
                stylesheet=self.styleSheet()
            )
