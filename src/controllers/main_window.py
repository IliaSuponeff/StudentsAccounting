"""
Contains class which exercises control over views.windows.ui_main_window.Ui_MainWindow

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime
import sys

from PySide6.QtWidgets import QMainWindow, QHeaderView, QListWidgetItem, QLabel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QDate
from views.windows.ui_main_window import Ui_MainWindow
from controllers.handler_manager import HandlerManager, DataBase, RuntimeSettings
from controllers.filter_manager import FilterType, FilterManager
from controllers.add_student_dialog import AddStudentDialog
from controllers.add_student_visit_dialog import AddStudentVisitDialog
from controllers.user_exception_mgs_dialogs import exception
from controllers.datechoose_dialog import DateChooseDialog


class MainWindowHandler(QMainWindow):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()

        self.settings = settings
        self.db = database
        self._dialogs = {
            "AddStudentVisitDialog": AddStudentVisitDialog(self.settings, self.db),
            "AddStudentDialog": AddStudentDialog(self.settings, self.db),
            "DateChooseDialog": DateChooseDialog(self.settings, self.db)
        }
        self._handler_manager = HandlerManager(settings, database)
        self._table_modal = QStandardItemModel()
        self._filter_manager = FilterManager()
        self._ui = Ui_MainWindow()
        self.setUi()
        self.setHandlers()

    def setUi(self):
        self._ui.setupUi(self)
        self.setIcons()
        self._ui.student_visits_table_view.setModel(self._table_modal)
        self._load_custom_period_view()
        self._reload_students()

    def setHandlers(self):
        self._ui.del_student_btn.clicked.connect(lambda: self._delete_student())
        self._ui.next_student_btn.clicked.connect(lambda: self._next_student())
        self._ui.prev_student_btn.clicked.connect(lambda: self._prev_student())
        self._ui.reload_student_btn.clicked.connect(lambda: self._get_box_student())
        self._ui.add_student_btn.clicked.connect(
            lambda: self._call_dialog('AddStudentDialog')
        )
        self._ui.add_visit_btn.clicked.connect(
            lambda: self._call_dialog('AddStudentVisitDialog', self._handler_manager.get_current_student())
        )
        self._ui.del_visit_btn.clicked.connect(lambda: self._delete_student_visit())
        self._ui.all_days_filter_rbtn.clicked.connect(
            lambda: self._set_filter_type(FilterType.ALL_DAYS)
        )
        self._ui.this_year_filter_rbtn.clicked.connect(
            lambda: self._set_filter_type(FilterType.THIS_YEAR)
        )
        self._ui.this_month_filter_rbtn.clicked.connect(
            lambda: self._set_filter_type(FilterType.THIS_MONTH)
        )
        self._ui.custom_period_rbtn.clicked.connect(
            lambda: self._set_filter_type(FilterType.CUSTOM_PERIOD)
        )
        self._ui.choose_from_date_btn.clicked.connect(
            lambda: self._change_date('from')
        )
        self._ui.choose_to_date_btn.clicked.connect(
            lambda: self._change_date('to')
        )

    def setIcons(self):
        self._ui.add_student_btn.setIcon(
            self.settings.load_image('add_student.png')
        )
        self._ui.add_visit_btn.setIcon(
            self.settings.load_image('add_visit.png')
        )

        # self._ui.edit_student_btn.setIcon(
        #     self.settings.load_image('edit.png')
        # )
        # self._ui.edit_visit_btn.setIcon(
        #     self.settings.load_image('edit.png')
        # )
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
        self._load_custom_period_view()
        self._load_current_student()
        self._load_summary_students_results()

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
        self._ui.student_summary_result_lbl.setText('')
        self._ui.student_currency_lbl.setText(
            student.currency().value if student is not None else ''
        )
        if student is not None:
            self._load_current_student_visits()

    def _load_current_student_visits(self):
        student = self._handler_manager.get_current_student()
        self._rebuild_table_modal()
        self._set_custom_filter()
        visits = self._filter_manager.filtrate(
            self._handler_manager.get_current_student_visits()
        )
        summary = 0
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

            if visit.is_special():
                summary += visit.special_sum()
            else:
                summary += visit.timespan() * student.hour_cost()

        self._ui.student_summary_result_lbl.setText(str(summary))

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

    def _call_dialog(self, _dialog_class_name: str, *args):
        if not (_dialog_class_name in self._dialogs.keys()):
            return

        if self._dialogs[_dialog_class_name] is None:
            return

        try:
            dialog = self._dialogs[_dialog_class_name]
            dialog.call(*args)
            dialog.show()
            dialog.exec()
            self._reload_students()
        except Exception as ex:
            exception(self.windowIcon(), '\n'.join([str(item) for item in ex.args]))

    def _delete_student_visit(self):
        indexes = tuple(self._get_selected_rows())
        if len(indexes) == 0:
            return

        self._handler_manager.delete_current_student_visit(indexes[0])
        self._reload_students()

    def _get_selected_rows(self) -> frozenset[int]:
        indexes = self._ui.student_visits_table_view.selectedIndexes()
        return frozenset([index.row() for index in indexes])

    def _set_custom_filter(self):
        if not (self._filter_manager.fiter_type() == FilterType.CUSTOM_PERIOD):
            return

        from_date = self._get_date_from_label(
            self._ui.from_date_lbl
        )
        to_date = self._get_date_from_label(
            self._ui.to_date_lbl
        )
        try:
            self._filter_manager.set_custom_period(from_date, to_date)
        except Exception as ex:
            exception(
                self.windowIcon(),
                msg='\n'.join([str(arg) for arg in ex.args])
            )

    def _set_filter_type(self, filter_type: FilterType):
        self._filter_manager.update_filter_type(filter_type)
        self._reload_students()

    def _load_summary_students_results(self):
        currencies = self._get_all_currencies_results()
        self._ui.results_all_students_list.clear()

        for currency in currencies:
            if currencies[currency] == 0:
                continue

            list_item = QListWidgetItem(
                f'{currencies[currency]} {currency}'
            )
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self._ui.results_all_students_list.addItem(list_item)

    def _get_all_currencies_results(self) -> dict[str, int]:
        currencies = {}
        for student in self._handler_manager.get_students():
            visits_summary_result = 0
            visits = self._filter_manager.filtrate(
                self._handler_manager.get_student_visits(student)
            )
            for visit in visits:
                if visit.is_special():
                    visits_summary_result += visit.special_sum()
                else:
                    visits_summary_result += visit.timespan() * student.hour_cost()

            currency = student.currency().value
            if currency in currencies.keys():
                currencies[currency] += visits_summary_result
            else:
                currencies[currency] = visits_summary_result

        return currencies

    def _load_custom_period_view(self):
        custom_period = self._filter_manager.get_custom_period()
        self._ui.from_date_lbl.setText(
            custom_period[0].strftime('%d.%m.%Y')
        )
        self._ui.to_date_lbl.setText(
            custom_period[1].strftime('%d.%m.%Y')
        )

    def _change_date(self, _change_type):
        date: QDate = self._get_qdate_by_type(_change_type)
        self._call_dialog('DateChooseDialog', date)
        choose_date_dialog: DateChooseDialog = self._dialogs['DateChooseDialog']
        new_date = choose_date_dialog.get_date()
        if new_date == date:
            return

        new_date = datetime.datetime.strptime(
            f'{new_date.day()}.{new_date.month()}.{new_date.year()}',
            '%d.%m.%Y'
        ).date()
        custom_period = list(self._filter_manager.get_custom_period())
        _index = 0 if _change_type == 'from' else 1
        custom_period[_index] = new_date
        custom_period.sort()
        self._filter_manager.set_custom_period(*custom_period)
        self._reload_students()

    @staticmethod
    def _get_date_from_label(lbl: QLabel) -> datetime.date:
        return datetime.datetime.strptime(
            lbl.text(),
            '%d.%m.%Y'
        ).date()

    def _get_qdate_by_type(self, _change_type) -> QDate:
        date = self._get_date_from_label(
            self._ui.from_date_lbl if _change_type == 'from' else self._ui.to_date_lbl
        )
        return QDate(date.year, date.month, date.day)
