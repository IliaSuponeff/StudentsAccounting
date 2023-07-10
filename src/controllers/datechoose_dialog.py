"""
Contains class which exercises control over views.dialogs.ui_date_choose.Ui_DateChoose

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from settings import RuntimeSettings
from controllers.database import DataBase
from views.dialogs.ui_date_choose import Ui_DateChoose


class DateChooseDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.db = database
        self._ui = Ui_DateChoose()
        self._ui.setupUi(self)

    def call(self, date: QDate, *args):
        self._ui.calendar.setSelectedDate(date)
        self.setHandlers()

    def setHandlers(self):
        self._ui.done_btn.clicked.connect(self.close)

    def get_date(self) -> QDate:
        return self._ui.calendar.selectedDate()
