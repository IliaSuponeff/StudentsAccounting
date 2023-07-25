"""
<INFO>

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import os.path
from PySide6.QtWidgets import QDialog
from settings import RuntimeSettings
from views.dialogs.ui_more_student_info_dialog import Ui_MoreInfoDialog


class MoreInfoDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, *args):
        super().__init__()
        self._settings = settings
        self._ui = Ui_MoreInfoDialog()
        self._ui.setupUi(self)
        self.setHandlers()

    def call(self, *args):
        self.setUi()

    def setUi(self):
       pass

    def setHandlers(self):
        pass

