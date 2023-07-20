"""
<INFO>

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from PySide6.QtWidgets import QDialog
from settings import RuntimeSettings
from views.dialogs.ui_help_dialog import Ui_HelpDialog


class HelpDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, *args):
        super().__init__()
        self._settings = settings
        self._ui = Ui_HelpDialog()
        self._ui.setupUi(self)

    def call(self, *args):
        self.setUi()

    def setUi(self):
        self.setWindowTitle('Помощь')
        self._ui.info_lbl_1.setText(self.windowTitle())

        self.setStyleSheet(self._settings.get_stylesheet(self._settings.STYLESHEET))

    def setHandlers(self):
        self._ui.close_btn.clicked.connect(lambda: self.close())