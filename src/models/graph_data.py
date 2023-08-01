"""
<INFO>

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import datetime


class GraphData:

    def __init__(self, value: int | float, date: datetime.date):
        self._value = float(value)
        self._date = date

    def date(self) -> datetime.date:
        return self._date

    def value(self) -> float:
        return self._value

    def __eq__(self, other):
        if other is None:
            return False

        if other is self:
            return True

        if not isinstance(other, self.__class__):
            return False

        return other.value() == self.value() and other.date() == self.date()

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __hash__(self) -> int:
        _hash = hash(self.__class__.__name__)
        _hash = 31 * _hash + hash(self.value())
        _hash = 31 * _hash + hash(self.date())
        return _hash

    def __lt__(self, other):
        if other is None:
            return True

        if other is self:
            return False

        if not isinstance(other, self.__class__):
            return False

        return self.date() < other.date()

    def __str__(self):
        return f"({self.value()}; {self.date()})"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__str__()}"
