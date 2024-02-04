from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from controllers.handler_manager import HandlerManager, RuntimeSettings
from models.student import Student
from views.dialogs.ui_search_student_dialog import Ui_SearchStudentDialog
from models.currency import Currency


class SearchStudentDialog(QDialog):
    _DEFAULT_CURRENCY = 'Все валюты'

    def __init__(self, settings: RuntimeSettings, handler_manager: HandlerManager) -> None:
        super().__init__()
        self._settings = settings
        self._handler_manager = handler_manager
        self._ui = Ui_SearchStudentDialog()
        self._students = self._handler_manager.get_students()
        self._setUI()

    def _setUI(self):
        self._ui.setupUi(self)
        self._ui.currency_box.addItems(
            [self._DEFAULT_CURRENCY] + [currency.value for currency in Currency]
        )

        if self._ui.currency_box.lineEdit() is not None:
            self._ui.currency_box.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
            self._ui.currency_box.lineEdit().setReadOnly(True)

        self._ui.students_list.setIconSize(QSize(64, 64))

        self._ui.student_name_le.textChanged.connect(self._change_name)
        self._ui.currency_box.currentTextChanged.connect(self._change_currency)
        self._ui.students_list.itemDoubleClicked.connect(self._update_current_student)

    def call(self, *args, **kwargs) -> None:
        self._students = self._handler_manager.get_students()
        self._ui.currency_box.setCurrentText(self._DEFAULT_CURRENCY)
        self._ui.student_name_le.setText('')
        self._reload_students()

    def _change_currency(self, currency_name: str):
        self._students = self._handler_manager.get_students()
        self._students = list(
            filter(
                lambda student: self._ui.student_name_le.text().strip().lower() in student.name().lower(),
                self._students
            )
        )

        if currency_name == self._DEFAULT_CURRENCY:
            return

        self._students = list(filter(lambda student: student.currency().value == currency_name, self._students))
        self._reload_students()

    def _change_name(self, new_text):
        currency_name = self._ui.currency_box.currentText()
        self._students = self._handler_manager.get_students()

        if currency_name != self._DEFAULT_CURRENCY:
            self._students = list(
                filter(
                    lambda student: student.currency().value == currency_name,
                    self._students
                )
            )

        self._students = list(
            filter(
                lambda student: new_text.strip().lower() in student.name().lower(),
                self._students
            )
        )
        self._reload_students()

    def _reload_students(self):
        self._ui.students_list.clear()
        for student in self._students:
            item = QListWidgetItem(
                self._settings.load_image('student.png'),
                f"Имя: {student.name()}\nВалюта: {student.currency().value}"
            )
            setattr(item, "__student__", student)
            self._ui.students_list.addItem(item)

    def _update_current_student(self, item: QListWidgetItem):
        if not hasattr(item, "__student__"):
            return

        student: Student = getattr(item, "__student__")
        self._handler_manager.set_current_student(student)
        self.close()