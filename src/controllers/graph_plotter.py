"""
<INFO>

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import PySide6.QtCharts
from PySide6.QtCore import Qt, QDate, QDateTime, QTime, QPointF, QMargins
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtGui import QColor, QPen

from controllers.filter_manager import FilterManager, FilterType
from models.currency import Currency
from models.graph_data import GraphData


class LinearGraphPlotter(QChart):

    def __init__(self, name, _filter: FilterManager):
        super().__init__()
        self.setObjectName(name)
        self.filter_manager = _filter
        self.legend().hide()
        self.setMargins(QMargins(10, 10, 10, 10))

    def updateData(self, title: str, data: list[GraphData]):
        if len(data) == 0:
            self._clear()
            return

        _series = QLineSeries()
        pen = QPen(
            QColor('blue'),
            5,
            Qt.PenStyle.SolidLine,
            Qt.PenCapStyle.RoundCap,
            Qt.PenJoinStyle.RoundJoin
        )
        _series.setPen(pen)

        data = self._prebuild_data(data)
        points: tuple[QPointF] = data['points']

        for point in points:
            _series.append(point)

        self._clear()
        self.addSeries(_series)
        self.createDefaultAxes()
        self._update_axis(title, data)

    def _update_axis(self, y_axis_title: str, data: dict):
        x_axis: QValueAxis = self.axisX()
        x_axis.setLabelFormat("%d")
        x_axis.setTitleText(data['date-title'])
        x_axis.setTickCount(data['length'] if data['length'] > 0 else int(10 + 1))
        x_axis.setRange(data['x-axis']['min'], data['x-axis']['max'])

        y_axis: QValueAxis = self.axisY()
        y_axis.setLabelFormat("%.1f")
        y_axis.setTitleText(y_axis_title)
        y_axis.setTickCount(10 + 1)
        y_axis.setRange(
            data['y-axis']['min'],
            data['y-axis']['max']
        )

    def _prebuild_data(self, input_data: list[GraphData]):
        fiter_type: FilterType = self.filter_manager.fiter_type()
        min_date = input_data[0].date()
        max_date = input_data[-1].date()
        date_title = ''

        points: tuple[QPointF] = ()
        if fiter_type == FilterType.ALL_DAYS:
            if abs(max_date.year - min_date.year) == 0:
                fiter_type = FilterType.CUSTOM_PERIOD
            else:
                points = self._get_all_years_points(
                    range(min_date.year, max_date.year + 1),
                    input_data
                )
                date_title = "Года"

        if fiter_type == FilterType.THIS_YEAR:
            if abs(max_date.month - min_date.month) == 0:
                fiter_type = FilterType.CUSTOM_PERIOD
            else:
                points = self._get_year_points(
                    range(1, 12 + 1),
                    input_data
                )
                date_title = f"Месяца {max_date.year} года"

        if fiter_type == FilterType.THIS_MONTH:
            points = self._get_moths_points(
                range(1, self.filter_manager.get_max_day(max_date.year, max_date.month)),
                input_data
            )
            date_title = f"Дни {min_date.month} месяца {max_date.year} года"

        if fiter_type == FilterType.CUSTOM_PERIOD:
            custom_result: tuple = self._get_custom_period_points(input_data)
            points = custom_result[0]
            date_title = custom_result[1]

        data = {
            "x-axis": {
                "min": min([point.x() for point in points]),
                "max": max([point.x() for point in points])
            },
            "y-axis": {
                "min": min([point.y() for point in points]),
                "max": max([point.y() for point in points])
            },
            "fiter-type": fiter_type,
            "length": len(points),
            "points": points,
            'date-title': date_title
        }
        return data

    @staticmethod
    def _get_all_years_points(_years_range, input_data: list[GraphData]) -> tuple[QPointF]:
        points = []
        years_data = {}
        for year in _years_range:
            years_data.setdefault(year, 0.0)

        for graph_data in input_data:
            years_data.setdefault(graph_data.date().year, 0.0)
            years_data[graph_data.date().year] += graph_data.value()

        for year in sorted(years_data.keys()):
            points.append(
                QPointF(year, years_data[year])
            )

        return tuple(points)

    @staticmethod
    def _get_year_points(_months_range, input_data: list[GraphData]) -> tuple[QPointF]:
        points = []
        moths_data = {}
        for month in _months_range:
            moths_data.setdefault(month, 0.0)

        for graph_data in input_data:
            moths_data.setdefault(graph_data.date().month, 0.0)
            moths_data[graph_data.date().month] += graph_data.value()

        for month in sorted(moths_data.keys()):
            points.append(
                QPointF(month, moths_data[month])
            )

        return tuple(points)

    @staticmethod
    def _get_moths_points(_days_range, input_data: list[GraphData]) -> tuple[QPointF]:
        points = []
        days_data = {}
        for day in _days_range:
            days_data.setdefault(day, 0.0)

        for graph_data in input_data:
            days_data.setdefault(graph_data.date().day, 0.0)
            days_data[graph_data.date().day] += graph_data.value()

        for day in sorted(days_data.keys()):
            points.append(
                QPointF(day, days_data[day])
            )

        return tuple(points)

    def _get_custom_period_points(self, input_data) -> tuple[QPointF]:
        min_date = input_data[0].date()
        max_date = input_data[-1].date()

        if min_date.year != max_date.year:
            # have more than 1 year in chosen data
            return self._get_all_years_points(
                range(min_date.year, max_date.year + 1),
                input_data
            ), 'Года'

        # have 1 year in chosen data
        if min_date.month != max_date.month:
            # have more than 1 month in chosen data
            return self._get_year_points(
                range(min_date.month, max_date.month + 1),
                input_data
            ), f'Месяца {min_date.year} года'

        # have 1 month in chosen data
        return self._get_moths_points(
            range(1, self.filter_manager.get_max_day(max_date.year, max_date.month)),
            input_data
        ), f"Дни {max_date.month} месяца {max_date.year} года"

    def _clear(self):
        self.removeAllSeries()
        self.removeAxis(self.axisX())
        self.removeAxis(self.axisY())

    def removeAxis(self, axis: PySide6.QtCharts.QAbstractAxis) -> None:
        if axis is not None:
            axis.setGridLineVisible(False)
            axis.hide()

        super().removeAxis(axis)
