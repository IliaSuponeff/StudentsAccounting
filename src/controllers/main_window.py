"""
Contains class which exercises control over views.windows.ui_main_window.Ui_MainWindow

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from PySide6.QtWidgets import QMainWindow, QHeaderView, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from views.windows.ui_main_window import Ui_MainWindow
from controllers.handler_manager import HandlerManager, DataBase, RuntimeSettings

from controllers.add_student_dialog import AddStudentDialog
from controllers.add_student_visit_dialog import AddStudentVisitDialog
from controllers.user_exception_mgs_dialogs import exception, warning


class MainWindowHandler(QMainWindow):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()
        self.settings = settings
        self.db = database
        self._handler_manager = HandlerManager(settings, database)
        self._table_modal = QStandardItemModel()
        self._ui = Ui_MainWindow()
        self.setUi()
        self.setHandlers()

    def setUi(self):
        self._ui.setupUi(self)
        self.setIcons()
        self._ui.student_visits_table_view.setModel(self._table_modal)
        self._reload_students()

    def setHandlers(self):
        self._ui.del_student_btn.clicked.connect(lambda: self._delete_student())
        self._ui.next_student_btn.clicked.connect(lambda: self._next_student())
        self._ui.prev_student_btn.clicked.connect(lambda: self._prev_student())
        self._ui.reload_student_btn.clicked.connect(lambda: self._get_box_student())
        self._ui.add_student_btn.clicked.connect(
            lambda: self._call_dialog(AddStudentDialog)
        )
        self._ui.add_visit_btn.clicked.connect(
            lambda: self._call_dialog(AddStudentVisitDialog, self._handler_manager.get_current_student())
        )
        self._ui.del_visit_btn.clicked.connect(lambda: self._delete_student_visit())

    def setIcons(self):
        self._ui.add_student_btn.setIcon(
            self.settings.load_image('add_student.png')
        )
        self._ui.add_visit_btn.setIcon(
            self.settings.load_image('add_visit.png')
        )
        self._ui.edit_student_btn.setIcon(
            self.settings.load_image('edit.png')
        )
        self._ui.edit_visit_btn.setIcon(
            self.settings.load_image('edit.png')
        )
        self._ui.next_student_btn.setIcon(
            self.settings.load_image('next_student.png')
        )
        self._ui.prev_student_btn.setIcon(
            self.settings.load_image('prev_student.png')
        )
        self._ui.reload_student_btn.setIcon(
            self.settings.load_image('reload.png')
        )
        self._ui.del_student_btn.setIcon(
            self.settings.load_image('remove_student.png')
        )
        self._ui.del_visit_btn.setIcon(
            self.settings.load_image('remove_visit.png')
        )

    def _reload_students(self):
        self._ui.student_choose_box.clear()
        self._rebuild_table_modal()
        self._ui.student_choose_box.addItems(
            [student.name() for student in self.db.students]
        )
        self._load_current_student()

    def _rebuild_table_modal(self):
        self._table_modal.clear()
        self._table_modal.setHorizontalHeaderLabels(
            ['Date', 'Timespan', 'Summary']
        )
        self._ui.student_visits_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._ui.student_visits_table_view.verticalHeader().hide()

    def _load_current_student(self):
        student = self._handler_manager.get_current_student()
        if student is not None:
            self._ui.student_choose_box.setCurrentText(
                student.name()
            )

        self._ui.student_name_lbl.setText(
            student.name() if student is not None else '-'
        )
        self._ui.student_summary_result_lbl.setText(str(
            self._handler_manager.get_current_student_summary_result()
        ) if student is not None else '')
        self._ui.student_currency_lbl.setText(
            student.currency().value if student is not None else ''
        )
        self._load_current_student_visits()

    def _load_current_student_visits(self):
        self._rebuild_table_modal()
        visits = self._handler_manager.get_current_student_visits()
        for visit in visits:
            row = [
                QStandardItem(str(visit.date().strftime('%d.%m.%Y'))),
                QStandardItem(str(visit.timespan())),
                QStandardItem(
                    str(
                        visit.special_sum()
                        if visit.is_special() else
                        self._handler_manager.get_current_student().hour_cost() * visit.timespan()
                    )
                )
            ]
            for item in row:
                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )
            self._table_modal.appendRow(row)

    def _delete_student(self):
        self._handler_manager.delete_current_student()
        self._reload_students()

    def _next_student(self):
        self._handler_manager.next_student()
        self._reload_students()

    def _prev_student(self):
        self._handler_manager.prev_student()
        self._reload_students()

    def _get_box_student(self):
        self._handler_manager.set_current_index(self._ui.student_choose_box.currentIndex())
        self._reload_students()

    def _call_dialog(self, _dialog_class_link, *args):
        try:
            dialog: QDialog = _dialog_class_link(self.settings, self.db, *args)
            dialog.show()
            dialog.exec()
            del dialog
            self._reload_students()
        except Exception as ex:
            exception(self.windowIcon(), '\n'.join([str(item) for item in ex.args]))

    def _delete_student_visit(self):
        indexes = tuple(self._get_selected_rows())
        if len(indexes) == 0:
            return

        self._handler_manager.delete_current_student_visit(indexes[0] + 1)
        self._reload_students()

    def _get_selected_rows(self) -> frozenset[int]:
        indexes = self._ui.student_visits_table_view.selectedIndexes()
        return frozenset([index.row() for index in indexes])
