"""
Contains a Visit class describing the student's presence model in the database records

version: 1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime


class Visit:
    _DATE: datetime.date = datetime.date.today()
    _TIMESPAN: float = 1
    _IS_SPECIAL: int = 0
    _SPECIAL_SUM: float = 0

    def __init__(self, date, timespan, is_special, special_sum):
        self.set_date(date)
        self.set_timespan(timespan)
        self.set_specialised_type(is_special, special_sum)

    def date(self) -> datetime.date:
        return self._DATE

    def timespan(self) -> float:
        return self._TIMESPAN

    def is_special(self) -> int:
        return self._IS_SPECIAL

    def special_sum(self) -> float:
        return self._SPECIAL_SUM

    @staticmethod
    def _is_date(date: str):
        if date is None:
            return False

        if isinstance(date, (datetime.datetime, datetime.date,)):
            return True

        if isinstance(date, str):
            try:
                datetime.datetime.strptime(date, '%d.%m.%Y')
                return True
            except ValueError as _:
                return False

        return False

    def set_date(self, date):
        if isinstance(date, (datetime.datetime, datetime.date,)):
            self._DATE = date.date() if isinstance(date, datetime.datetime) else date

        if isinstance(date, str):
            self._DATE = datetime.datetime.strptime(date, '%d.%m.%Y').date()

    def set_timespan(self, timespan):
        assert timespan > 0, f'Неверная длительность занятия. Оно должно быть больше 0'
        self._TIMESPAN = float(timespan)

    @staticmethod
    def _is_number(timespan):
        if timespan is None:
            return False

        if not isinstance(timespan, (int, float,)):
            return False

        return True

    def set_specialised(self, is_special):
        is_special = bool(is_special)
        self._IS_SPECIAL = 1 if is_special else 0

    def set_special_sum(self, special_sum):
        if bool(self._IS_SPECIAL) and special_sum < 0:
            raise AttributeError(f'Так, как цена договорная, то и стоимость урока должна быть больше 0')

        self._SPECIAL_SUM = float(special_sum) if self._IS_SPECIAL else 0

    def set_specialised_type(self, is_special, special_sum):
        self.set_specialised(is_special)
        self.set_special_sum(special_sum)

    def __eq__(self, o: object) -> bool:
        if o is None:
            return False

        if o is self:
            return True

        if not isinstance(o, self.__class__):
            return False

        if o.date() != self.date():
            return False

        if o.timespan() != self.timespan():
            return False

        return self.is_special() == o.is_special() and self.special_sum() == o.special_sum()

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __str__(self) -> str:
        return f'Visit<date={self.date()} timespan={self.timespan()} ' \
               f'is-special={self.is_special()} special-sum={self.special_sum()}>'

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        _hash = hash(self.__class__.__name__)
        _hash = 31 * _hash + hash(self.date())
        _hash = 31 * _hash + hash(self.timespan())
        _hash = 31 * _hash + hash(self.is_special())
        _hash = 31 * _hash + hash(self.special_sum())
        return _hash

    def __lt__(self, other):
        if other is None:
            return True

        if not isinstance(other, self.__class__):
            return False

        if other is self:
            return False

        if self.date() < other.date():
            return True

        return False
