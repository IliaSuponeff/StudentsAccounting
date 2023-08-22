"""
<INFO>

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime

from PySide6.QtCharts import QChartView, QChart
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QDialog

from controllers.database import DataBase
from controllers.filter_manager import FilterManager
from controllers.graph_plotter import BarGraphPlotter
from controllers.handler_manager import HandlerManager
from models.currency import Currency
from models.graph_data import GraphData
from models.student import Student
from models.student_visit import Visit
from settings import RuntimeSettings
from views.dialogs.ui_more_student_info_dialog import Ui_MoreInfoDialog


class MoreInfoDialog(QDialog):
    _PLOT_TYPES = (
        'Сумма заработка',
        "Длительность занятий"
    )

    def __init__(
            self,
            settings: RuntimeSettings,
            database: DataBase,
            handler_manager: HandlerManager,
            filter_manager: FilterManager
    ):
        super().__init__()
        self._settings = settings
        self._db = database
        self._handler_manager = handler_manager
        self._filter = filter_manager

        # init UI components
        self._ui = Ui_MoreInfoDialog()
        self._plotter = BarGraphPlotter("SummaryPlotter", self._settings, self._filter)
        self._chart_view = QChartView(self._plotter)

        # init UI and handlers
        self._set_ui()
        self.setHandlers()

    def show(self) -> None:
        super().show()

    def call(self, *args: object):
        assert len(self._handler_manager.get_students()) > 0, \
            "Нет учеников для вывода подробной информации"
        self._updateUI()

    def _updateUI(self):
        self.setWindowTitle("Подробная информация  доходах")
        valid_period = self._filter.get_period_now()

        self._ui.fiter_period_info_lbl.setText(
            f'За период с {valid_period[0]} по {valid_period[1]} для'
            if len(valid_period) > 0 else "За все дни"
        )

        self._plotter.removeAllSeries()
        self._plotter.removeAxis(self._plotter.axisX())
        self._plotter.removeAxis(self._plotter.axisY())
        self._plotter.setTheme(
            QChart.ChartTheme.ChartThemeLight
            if self._settings.STYLESHEET == 'light' else
            QChart.ChartTheme.ChartThemeDark
        )

        self._ui.all_students_check_rbtn.setChecked(True)
        self._ui.student_choose_frame.hide()

        self._ui.student_choose_box.clear()
        self._ui.student_choose_box.addItems(
            [str(student.name()) for student in self._handler_manager.get_students()]
        )
        self._ui.student_choose_box.setCurrentText(
            self._handler_manager.get_current_student().name()
        )
        self._ui.student_choose_box.show()

        self._load_theme_icons()
        self.setStyleSheet(self._settings.get_stylesheet(
            self._settings.STYLESHEET
        ))
        self._reload_graphs()

    def setHandlers(self):
        self._ui.all_students_check_rbtn.clicked.connect(
            lambda: self._reload(reload_all_players=True)
        )
        self._ui.one_student_check_rbtn.clicked.connect(
            lambda: self._reload(reload_all_players=False)
        )
        self._ui.next_student_btn.clicked.connect(lambda: self._next_student())
        self._ui.prev_student_btn.clicked.connect(lambda: self._prev_student())
        self._ui.reload_student_btn.clicked.connect(lambda: self._get_box_student())
        self._ui.plot_type_box.currentTextChanged.connect(lambda text: self._reload_graphs())
        self._ui.currency_choose_box.currentTextChanged.connect(lambda text: self._reload_graphs())

    def _next_student(self):
        self._handler_manager.next_student()
        self._ui.student_choose_box.setCurrentText(
            self._handler_manager.get_current_student().name()
        )
        self._reload_graphs()

    def _prev_student(self):
        self._handler_manager.prev_student()
        self._ui.student_choose_box.setCurrentText(
            self._handler_manager.get_current_student().name()
        )
        self._reload_graphs()

    def _get_box_student(self):
        self._handler_manager.set_current_index(self._ui.student_choose_box.currentIndex())
        self._ui.student_choose_box.setCurrentText(
            self._handler_manager.get_current_student().name()
        )
        self._reload_graphs()

    def _set_ui(self):
        self._ui.setupUi(self)
        self._chart_view.setRenderHint(QPainter.RenderHint.TextAntialiasing | QPainter.RenderHint.Antialiasing)
        self._ui.plot_layout.addWidget(
            self._chart_view
        )
        self._ui.student_choose_box.setEditable(True)
        self._ui.student_choose_box.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._ui.student_choose_box.lineEdit().setReadOnly(True)

        self._ui.plot_type_box.setEditable(True)
        self._ui.plot_type_box.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._ui.plot_type_box.lineEdit().setReadOnly(True)

        self._ui.currency_choose_box.setEditable(True)
        self._ui.currency_choose_box.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._ui.currency_choose_box.lineEdit().setReadOnly(True)

        self._ui.plot_type_box.clear()
        self._ui.plot_type_box.addItems(list(self._PLOT_TYPES))
        self._ui.currency_choose_box.clear()
        self._ui.currency_choose_box.addItems(
            [str(currency) for currency in Currency]
        )

        # self._updateUI()

    def _load_theme_icons(self):
        self._ui.next_student_btn.setIcon(
            self._settings.load_theme_image('next_student.png')
        )
        self._ui.prev_student_btn.setIcon(
            self._settings.load_theme_image('prev_student.png')
        )
        self._ui.reload_student_btn.setIcon(
            self._settings.load_theme_image('reload.png')
        )

    def _reload(self, reload_all_players: bool = True):
        reload_all_players = bool(reload_all_players)
        if reload_all_players:
            self._ui.student_choose_frame.hide()
            self._ui.currency_choose_frame.show()
        else:
            self._ui.student_choose_frame.show()
            self._ui.currency_choose_frame.hide()

        self._reload_graphs()

    def _reload_graphs(self):
        all_visits: list[Visit] = self._get_visits()
        currencies = self._build_currency_dict(dict)

        for visit in all_visits:
            date = visit.date()
            student: Student = visit.__getattribute__('student')
            currency = student.currency()
            dates: dict = currencies[currency]

            # dates[date] = [<summary-value>, <timespan-value>]
            dates.setdefault(date, [0.0, 0.0])

            timespan = visit.timespan()
            summary = visit.special_sum()

            if not visit.is_special():
                summary = timespan * student.hour_cost()

            data = dates[date]
            dates[date] = [data[0] + summary, data[1] + timespan]

        need_currency = Currency.get_currency(self._ui.currency_choose_box.currentText())
        if not self._ui.all_students_check_rbtn.isChecked():
            need_currency = self._handler_manager.get_current_student().currency()

        vals: dict[datetime.date, list[float, float]] = currencies[need_currency]
        vals_type_index = self._PLOT_TYPES.index(self._ui.plot_type_box.currentText())

        graph_datas = []
        dates: list[datetime.date] = list(vals.keys())
        for date in dates:
            graph_datas.append(
                GraphData(
                    vals[date][vals_type_index],
                    date
                )
            )

        vals_axis_title = f'{self._ui.plot_type_box.currentText()} ' \
                          f'({need_currency if vals_type_index == 0 else "часы"})'
        self._plotter.updateData(vals_axis_title, graph_datas)

    @staticmethod
    def _build_currency_dict(_type=list) -> dict[Currency, list]:
        _dict = {}
        for currency in Currency:
            _dict[currency] = _type()

        return _dict

    def _get_visits(self):
        all_students_load = self._ui.all_students_check_rbtn.isChecked()
        students: list[Student] = [self._handler_manager.get_current_student()]
        if all_students_load:
            students: list[Student] = self._handler_manager.get_students()

        visits = list()
        for student in students:
            student_visits: list[Visit] = self._filter.filtrate(
                self._handler_manager.get_student_visits(student)
            )
            for visit in student_visits:
                visit.__setattr__('student', student)
                visits.append(visit)

        return tuple(visits)
