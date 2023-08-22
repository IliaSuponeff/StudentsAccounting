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
from controllers.database import DataBase, Visit
from controllers.user_exception_mgs_dialogs import exception


class AddStudentVisitDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.db = database
        self._student = None
        self._ui = Ui_CreatorVisit()
        self._ui.setupUi(self)
        self.setHandlers()

    def setUi(self):
        self.setWindowTitle(f'Добавить посещения ученику {self._student.name()}')
        self._ui.dialog_title_lbl.setText(self.windowTitle())
        self._ui.img_lbl.setPixmap(
            self.settings.load_pixmap('create_visit.png')
        )
        date_now = datetime.date.today()
        self._ui.visit_date_edit.setDate(
            QDate(date_now.year, date_now.month, date_now.day)
        )
        self._ui.timespan_spinbox.setValue(1.0)
        self._ui.currency_lbl.setText(self._student.currency().value)
        self._ui.unspecial_rbtn.setChecked(True)
        self._ui.special_sum_frame.hide()
        self._ui.sp_sum_spinbox.setValue(0.0)
        self.setStyleSheet(self.settings.get_stylesheet(self.settings.STYLESHEET))

    def setHandlers(self):
        self._ui.unspecial_rbtn.clicked.connect(lambda: self._ui.special_sum_frame.hide())
        self._ui.special_rbtn.clicked.connect(lambda: self._ui.special_sum_frame.show())
        self._ui.done_btn.clicked.connect(lambda: self._add_visit())

    def call(self, student, *args):
        assert student is not None, "Нет ученика для добавления ему посещения"
        self._student = student
        self.setUi()

    def _add_visit(self):
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
                    f"Посещение на {visit.date().strftime('%d.%m.%Y')} длительностью {visit.timespan()} часом"
                    f"{f' и специальная цена {visit.special_sum()}' if visit.is_special() else ''} is exists now."
                )

            self.db.add_student_visit(self._student, visit)
            self.close()
        except Exception as ex:
            exception(
                icon=self.windowIcon(),
                msg='\n'.join([str(arg) for arg in ex.args]).strip(),
                stylesheet=self.styleSheet()
            )
