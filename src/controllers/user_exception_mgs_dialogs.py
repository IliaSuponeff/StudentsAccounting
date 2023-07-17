"""
Contains functions for calling dialog boxes with user errors

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


def _create_message_box(icon, inline_icon, title, msg, buttons):
    box = QMessageBox(
        inline_icon,
        str(title), str(msg),
        buttons,
    )

    if icon is not None and isinstance(icon, QIcon):
        box.setWindowIcon(icon)

    box.show()
    box.exec()
    return box


def exception(icon: QIcon, msg: str) -> QMessageBox:
    return _create_message_box(
        icon, QMessageBox.Icon.Critical, 'Ошибка', msg, QMessageBox.StandardButton.Ok
    )


def warning(icon: QIcon, msg: str) -> QMessageBox:
    return _create_message_box(
        icon, QMessageBox.Icon.Warning, 'Предупреждение', msg, QMessageBox.StandardButton.Ok
    )
