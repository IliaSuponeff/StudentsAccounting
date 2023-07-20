"""
<INFO>

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import os.path
import pprint

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from settings import RuntimeSettings
from views.dialogs.ui_info_dialog import Ui_InfoDialog


class AboutDialog(QDialog):

    def __init__(self, settings: RuntimeSettings, *args):
        super().__init__()
        self._settings = settings
        self._ui = Ui_InfoDialog()
        self._ui.setupUi(self)
        self.setHandlers()

    def call(self, *args):
        self.setUi()

    def setUi(self):
        self.setWindowTitle('О разработчике')
        self._ui.info_lbl_1.setText(self.windowTitle())

        help_data = '# Ошибка\n' \
                    'Информация о разработчике не найдена, утерян файл.'
        if os.path.exists(self._settings.get_resource_filepath('about.md')):
            data = self._settings.get_resources_filedata('about.md')
            if len(data) != 0:
                help_data = data

        self._ui.help_info_tb.setOpenExternalLinks(True)
        self._ui.help_info_tb.setMarkdown(
            str(help_data).strip() + '\n\n***\n\n' + str(self._get_youtube_link_text())
        )

        self.setStyleSheet(self._settings.get_stylesheet(self._settings.STYLESHEET))

    def setHandlers(self):
        self._ui.close_btn.clicked.connect(lambda: self.close())

    @staticmethod
    def _get_youtube_link_text():
        link = f'[__*YouTube*__](https://youtube.com/)'
        return f'Вы можете посмотреть **видео** на {link}, ' \
               f'где также описано, как пользоваться этим приложением.'
