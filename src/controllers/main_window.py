"""
Contains class which exercises control over views.windows.ui_main_window.Ui_MainWindow

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime
import sys

from PySide6.QtWidgets import (
    QMainWindow, QHeaderView,
    QLabel, QDialog
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QDate
from views.windows.ui_main_window import Ui_MainWindow
from controllers.handler_manager import HandlerManager, DataBase, RuntimeSettings
from controllers.filter_manager import FilterType, FilterManager
from controllers.add_student_dialog import AddStudentDialog
from controllers.add_student_visit_dialog import AddStudentVisitDialog
from controllers.user_exception_mgs_dialogs import exception
from controllers.datechoose_dialog import DateChooseDialog
from controllers.edit_student_dialog import EditStudentDialog
from controllers.edit_student_visit_dialog import EditStudentVisitDialog
from controllers.help_dialog import HelpDialog
from controllers.about_dialog import AboutDialog
from controllers.more_info_dialog import MoreInfoDialog
from models.student_visit import Visit


class MainWindowHandler(QMainWindow):

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        super().__init__()

        self.settings = settings
        self.db = database
        self._handler_manager = HandlerManager(settings, database)
        self._dialogs = {
            "AddStudentVisitDialog": AddStudentVisitDialog(self.settings, self.db),
            "AddStudentDialog": AddStudentDialog(self.settings, self.db),
            "EditStudentDialog": EditStudentDialog(self.settings, self.db),
            "EditStudentVisitDialog": EditStudentVisitDialog(self.settings, self.db),
            "DateChooseDialog": DateChooseDialog(self.settings, self.db),
            "HelpDialog": HelpDialog(self.settings),
            "AboutDialog": AboutDialog(self.settings),
            "MoreInfoDialog": MoreInfoDialog(self.settings, self.db, self._handler_manager)
        }
        self._visits_table_modal = QStandardItemModel()
        self._all_result_table_model = QStandardItemModel()
        self._filter_manager = FilterManager()
        self._ui = Ui_MainWindow()
        self._setWindowSettings()
        self.setUi()
        self.setHandlers()

    def _setWindowSettings(self):
        self.setWindowIcon(self.settings.load_image('icon.png'))
        self.setWindowTitle(self.settings.TITLE)

        for dialog_name in self._dialogs:
            dialog: QDialog = self._dialogs[dialog_name]
            dialog.setWindowIcon(self.windowIcon())

    def setUi(self):
        self._ui.setupUi(self)
        self.setIcons()
        self._ui.status_bar.showMessage(self.settings.get_app_status())
        self._set_theme(self.settings.STYLESHEET)
        self._ui.student_visits_table_view.setModel(self._visits_table_modal)
        self._ui.all_results_table_view.setModel(self._all_result_table_model)
        self._ui.student_choose_box.setEditable(True)
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
        self._ui.edit_student_btn.clicked.connect(
            lambda: self._call_dialog('EditStudentDialog', self._handler_manager.get_current_student())
        )
        self._ui.edit_visit_btn.clicked.connect(
            lambda: self._call_dialog(
                'EditStudentVisitDialog',
                self._handler_manager.get_current_student(),
                self._get_selected_visit()
            )
        )
        self._ui.help_btn.clicked.connect(
            lambda: self._call_dialog('HelpDialog')
        )
        self._ui.about_btn.clicked.connect(
            lambda: self._call_dialog('AboutDialog')
        )
        self._ui.more_info_btn.clicked.connect(
            lambda: self._call_dialog('MoreInfoDialog')
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
        self._ui.theme_change_btn.clicked.connect(lambda: self._change_theme())

    def setIcons(self):
        self._load_theme_icons()
        self._ui.img_lbl_1.setPixmap(
            self.settings.load_pixmap('filter.png')
        )
        self._ui.img_lbl_2.setPixmap(
            self.settings.load_pixmap('student_info.png')
        )
        self._ui.img_lbl_3.setPixmap(
            self.settings.load_pixmap('all_results.png')
        )

    def _reload_students(self):
        self._ui.student_choose_box.clear()
        self._ui.student_choose_box.addItems(
            [student.name() for student in self.db.students]
        )
        if self._ui.student_choose_box.lineEdit() is not None:
            # self._ui.student_choose_box.lineEdit().setReadOnly(False)
            self._ui.student_choose_box.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
            self._ui.student_choose_box.lineEdit().setReadOnly(True)

        self._rebuild_tables_modals()
        self._load_custom_period_view()
        self._load_filter_period_now()
        self._load_current_student()
        self._load_summary_students_results()

    def _rebuild_tables_modals(self):
        # visits table rebuild
        self._visits_table_modal.clear()
        self._visits_table_modal.setHorizontalHeaderLabels(
            ['Дата', 'Длительность', 'Сумма']
        )
        self._ui.student_visits_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._ui.student_visits_table_view.verticalHeader().hide()

        # all results table rebuild
        self._all_result_table_model.clear()
        self._ui.all_results_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._ui.all_results_table_view.horizontalHeader().hide()
        self._ui.all_results_table_view.verticalHeader().hide()

    def _load_current_student(self):
        student = self._handler_manager.get_current_student()
        if student is not None:
            self._ui.student_choose_box.setCurrentText(
                student.name()
            )

        self._ui.student_name_lbl.setText(
            student.name() if student is not None else 'Нет учеников'
        )
        self._ui.student_summary_result_lbl.setText('Нет информации')
        self._ui.summary_timespan_result_lbl.setText('Нет информации')
        if student is not None:
            self._load_current_student_visits()

    def _load_current_student_visits(self):
        student = self._handler_manager.get_current_student()
        self._rebuild_tables_modals()
        self._set_custom_filter()
        visits = self._filter_manager.filtrate(
            self._handler_manager.get_current_student_visits()
        )
        summary = 0
        sum_timespan = 0
        for visit in visits:
            row = [
                QStandardItem(str(
                    visit.date().strftime('%A')[:3]
                ) + '  ' + str(
                    visit.date().strftime('%d.%m.%Y')
                )),
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
                item.setEditable(False)

            self._visits_table_modal.appendRow(row)

            if visit.is_special():
                summary += visit.special_sum()
            else:
                summary += visit.timespan() * student.hour_cost()

            sum_timespan += visit.timespan()

        self._ui.student_summary_result_lbl.setText(
            f'{summary} {student.currency().value}'
        )
        self._ui.summary_timespan_result_lbl.setText(
            f'{round(sum_timespan, 1)} часов'
        )

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
            exception(self.windowIcon(), self.styleSheet(), '\n'.join([str(item) for item in ex.args]))

    def _delete_student_visit(self):
        indexes = tuple(self._get_selected_rows())
        if len(indexes) == 0:
            return

        self._handler_manager.delete_current_student_visit(indexes[0])
        self._reload_students()

    def _get_selected_rows(self) -> frozenset[int]:
        indexes = self._ui.student_visits_table_view.selectedIndexes()
        return frozenset([int(index.row()) for index in indexes])

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
                msg='\n'.join([str(arg) for arg in ex.args]),
                stylesheet=self.styleSheet()
            )

    def _set_filter_type(self, filter_type: FilterType):
        self._filter_manager.update_filter_type(filter_type)
        self._reload_students()

    def _load_summary_students_results(self):
        currencies = self._get_all_currencies_results()
        for currency in currencies:
            row = currencies[currency]
            if row[0] <= 0 or row[1] <= 0:
                continue

            row = [
                QStandardItem(f'{row[0]} {currency}'),
                QStandardItem(f'{round(row[1], 1)} часов')
            ]
            for item in row:
                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )
                item.setEditable(False)

            self._all_result_table_model.appendRow(row)

    def _get_all_currencies_results(self) -> dict[str, list]:
        currencies = {}
        for student in self._handler_manager.get_students():
            visits_summary_result = 0
            visits_timespan_summary_result = 0
            visits = self._filter_manager.filtrate(
                self._handler_manager.get_student_visits(student)
            )
            for visit in visits:
                if visit.is_special():
                    visits_summary_result += visit.special_sum()
                else:
                    visits_summary_result += visit.timespan() * student.hour_cost()

                visits_timespan_summary_result += visit.timespan()

            currency = student.currency().value
            if currency in currencies.keys():
                currencies[currency][0] += visits_summary_result
                currencies[currency][1] += visits_timespan_summary_result
            else:
                currencies[currency] = [visits_summary_result, visits_timespan_summary_result]

        return currencies

    def _load_custom_period_view(self):
        custom_period = self._filter_manager.get_custom_period()
        self._ui.from_date_lbl.setText(
            f"С {custom_period[0].strftime('%d.%m.%Y')}"
        )
        self._ui.to_date_lbl.setText(
            f"До {custom_period[1].strftime('%d.%m.%Y')}"
        )

    def _load_filter_period_now(self):
        period = self._filter_manager.get_period_now()
        if len(period) == 0:
            self._ui.period_info_lbl.setText("01.01.2001 - 31.12.9999")
            return

        from_date = period[0].strftime('%d.%m.%Y')
        to_date = period[1].strftime('%d.%m.%Y')
        self._ui.period_info_lbl.setText(
            f'{from_date} - {to_date}'
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
        text = lbl.text().split()[1]
        return datetime.datetime.strptime(
            text,
            '%d.%m.%Y'
        ).date()

    def _get_qdate_by_type(self, _change_type) -> QDate:
        date = self._get_date_from_label(
            self._ui.from_date_lbl if _change_type == 'from' else self._ui.to_date_lbl
        )
        return QDate(date.year, date.month, date.day)

    def _get_selected_visit(self) -> Visit:
        selected_row = tuple(self._get_selected_rows())
        if len(selected_row) == 0:
            return None

        visits = self._handler_manager.get_current_student_visits()
        return visits[selected_row[0]]

    def _set_theme(self, theme_name):
        if theme_name is None:
            self.setStyleSheet('')
            return

        if not self.settings.is_have_stylesheet(theme_name):
            print(f'Not found theme "{theme_name}" at local files', file=sys.stderr)
            return

        stylesheet = self.settings.get_stylesheet(theme_name)
        if len(stylesheet) == 0:
            print(f"Theme file '{theme_name}' is empty.", file=sys.stderr)
            return

        self.settings.STYLESHEET = theme_name
        self.setStyleSheet(stylesheet)
        self._ui.theme_change_btn.setIcon(
            self.settings.load_image(f'{theme_name}.png')
        )

    def _change_theme(self):
        if len(self.settings.STYLESHEET) == 0:
            self._set_theme(None)

        index = self.settings.__STYLESHEETS__.index(self.settings.STYLESHEET)
        index = (index + 1) % len(self.settings.__STYLESHEETS__)
        theme_name = self.settings.__STYLESHEETS__[index]
        self._set_theme(theme_name)
        self._load_theme_icons()

    def _load_theme_icons(self):
        self._ui.add_student_btn.setIcon(
            self.settings.load_theme_image('add_people.png')
        )
        self._ui.add_visit_btn.setIcon(
            self.settings.load_theme_image('add_visit.png')
        )

        self._ui.edit_student_btn.setIcon(
            self.settings.load_theme_image('edit.png')
        )
        self._ui.edit_visit_btn.setIcon(
            self.settings.load_theme_image('edit.png')
        )
        self._ui.next_student_btn.setIcon(
            self.settings.load_theme_image('next_student.png')
        )
        self._ui.prev_student_btn.setIcon(
            self.settings.load_theme_image('prev_student.png')
        )
        self._ui.reload_student_btn.setIcon(
            self.settings.load_theme_image('reload.png')
        )
        self._ui.del_student_btn.setIcon(
            self.settings.load_theme_image('remove_student.png')
        )
        self._ui.del_visit_btn.setIcon(
            self.settings.load_theme_image('remove_visit.png')
        )

    def close(self) -> bool:
        for _dialog_name in self._dialogs:
            _dialog: QDialog = self._dialogs[_dialog_name]
            _dialog.close()

        return super().close()
