"""
Contains class Filter, which can filtrate students visits by date-period

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime
import calendar
from models.filter_type import FilterType
from models.student_visit import Visit
from PySide6.QtCore import QDate


class FilterManager:
    _CUSTOM_DATE_PERIOD = (
        datetime.date.today(),
        datetime.date.today()
    )

    def __init__(self):
        self._filter_type = FilterType.ALL_DAYS
        self._CUSTOM_DATE_PERIOD = self._get_this_month_period()

    def update_filter_type(self, filter_type: str | FilterType):
        is_filter_type, value = FilterType.filter_type(filter_type)
        if is_filter_type:
            self._filter_type = value

    def set_custom_period(self, from_date: datetime.date, to_date: datetime.date):
        assert from_date is not None and isinstance(from_date, (datetime.date, QDate,)), \
            "Invalid custom filter date FROM"
        assert to_date is not None and isinstance(to_date, (datetime.date, QDate,)), \
            "Invalid custom filter date TO"

        from_date, to_date = self._normalized_dates(from_date, to_date)

        assert from_date <= to_date, "custom filter date FROM low than TO"
        self._CUSTOM_DATE_PERIOD = (
            from_date, to_date
        )

    def get_custom_period(self):
        return self._CUSTOM_DATE_PERIOD

    def filtrate(self, visits: list[Visit]):
        if visits is None or not isinstance(visits, (list, tuple, set, frozenset,)):
            return []

        filtrate_result = []
        for visit in visits:
            if not isinstance(visit, Visit):
                continue

            if self._is_valid_date(visit.date()):
                filtrate_result.append(visit)

        return filtrate_result

    def _get_this_month_period(self) -> tuple[datetime.date, datetime.date]:
        date = datetime.date.today()
        return (
            datetime.datetime.strptime(f'01.{date.month}.{date.year}', '%d.%m.%Y').date(),
            datetime.datetime.strptime(
                f'{self._get_max_day(date.year, date.month)}.{date.month}.{date.year}', '%d.%m.%Y'
            ).date()
        )

    def _get_this_year_period(self) -> tuple[datetime.date, datetime.date]:
        date = datetime.date.today()
        return (
            datetime.datetime.strptime(f'01.01.{date.year}', '%d.%m.%Y').date(),
            datetime.datetime.strptime(
                f'{self._get_max_day(date.year, 12)}.12.{date.year}', '%d.%m.%Y'
            ).date()
        )

    @staticmethod
    def _get_max_day(year: int, month: int):
        return calendar.monthrange(year, month)[1]

    def _is_valid_date(self, date: datetime.date):
        if self._filter_type == FilterType.ALL_DAYS:
            return True

        period = self._get_valid_filter_type_period()
        return period[0] <= date <= period[1]

    def _get_valid_filter_type_period(self) -> tuple[datetime.date, datetime.date]:
        if self._filter_type == FilterType.CUSTOM_PERIOD:
            return self.get_custom_period()

        if self._filter_type == FilterType.THIS_YEAR:
            return self._get_this_year_period()

        return self._get_this_month_period()

    def fiter_type(self) -> FilterType:
        return self._filter_type

    def _normalized_dates(self, from_date, to_date):
        return self._normalize_date(from_date), self._normalize_date(to_date)

    @staticmethod
    def _normalize_date(date: datetime.date | QDate):
        if isinstance(date, datetime.date):
            return date

        return datetime.datetime.strptime(
            f'{date.day()}.{date.month()}.{date.year()}',
            '%d.%m.%Y'
        ).date()

    def get_period_now(self):
        if self._filter_type == FilterType.ALL_DAYS:
            return ()

        if self._filter_type == FilterType.CUSTOM_PERIOD:
            return self.get_custom_period()

        if self._filter_type == FilterType.THIS_MONTH:
            return self._get_this_month_period()

        return self._get_this_year_period()
